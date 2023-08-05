import os
import re
from typing import List
from typing import Mapping
from jinja2 import Template
from .log_support import logger
from .support import MapperError, SqlAction
from .sql_support import is_dynamic_sql, get_named_sql_args

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

_SQL_CONTAINER = dict()
_valid_sql_actions = (SqlAction.INSERT.value, SqlAction.UPDATE.value, SqlAction.DELETE.value, SqlAction.SELECT.value)


class SqlModel:
    def __init__(self, sql: str, action: str, namespace: str, dynamic=False, includes: List[str] = None, pk_seq: str = None, select_key: str=None):
        self.sql = sql
        self.action = action
        self.namespace = namespace
        self.dynamic = dynamic
        self.includes = includes
        self.pk_seq = pk_seq
        self.select_key = select_key
        self.mapping = True if dynamic else ':' in sql
        self.placeholder = False if self.mapping else '?' in sql


def get_sql(sql_id: str, *args, **kwargs):
    sql_model = get_sql_model(sql_id)
    return do_get_sql(sql_model, False, None, *args, **kwargs)


def do_get_sql(sql_model, batch, param_names, *args, **kwargs):
    """
    Get sql from SqlModel.
    :param sql_model: SqlModel
    :param batch: bool, is batch or not
    :param param_names: original function parameter names
    :param args:
    :param kwargs:
    :return:
    """
    if sql_model.dynamic:
        if not kwargs:
            raise MapperError("Parameter 'kwargs' must not be empty when named mapping sql.")
        sql = sql_model.sql.render(**kwargs)
        logger.debug("Original sql: {}".format(sql))
        return get_named_sql_args(sql, **kwargs)
    else:
        logger.debug("Original sql: {}".format(sql_model.sql))
        if sql_model.mapping and kwargs:
            return get_named_sql_args(sql_model.sql, **kwargs)
        elif sql_model.placeholder and kwargs:
            logger.warning("Better use 'func(arg1, arg2...)' then 'func(arg1=arg1, arg2=arg2...)' if sql contain '?' placeholder.")
            args = [kwargs[name] for name in param_names if name in kwargs] if param_names else list(kwargs.values())
        elif sql_model.mapping and not kwargs and (not batch or
                                                   (batch and (not args or not isinstance(args[0], Mapping)))):  # batch_execute时args可能为List[Mapping]
            raise MapperError("Parameter 'kwargs' must not be empty when named mapping sql.")
        return sql_model.sql, args


def build_sql_id(namespace, _id):
    return namespace + "." + _id


def get_sql_model(sql_id: str):
    global _SQL_CONTAINER
    return _SQL_CONTAINER[sql_id]


# ----------------------------------------------------------Load mapper--------------------------------------------------------------------
def load_mapper(path: str):
    if os.path.isfile(path) and path.endswith(".xml"):
        _parse_mapper_file(path)
    elif os.path.isdir(path):
        for f in os.listdir(path):
            file = os.path.join(path, f)
            if os.path.isfile(file) and f.endswith(".xml"):
                _parse_mapper_file(file)
            elif os.path.isdir(file):
                load_mapper(file)


def _parse_mapper_file(file: str):
    global _SQL_CONTAINER
    tree = ET.parse(file)
    root = tree.getroot()
    namespace = root.attrib.get('namespace', '')
    results = list(map(lambda child: _load_sql(namespace, child, file), root))
    sql_ids, file_all_includes = zip(*results)
    for i, includes in enumerate(file_all_includes):
        if includes:
            for include in includes:
                if include not in sql_ids:
                    raise MapperError("Include '%s' are not exist in mapper file: %s" % (include, file))

                include_sql_id = build_sql_id(namespace, include)
                include_sql_model = _SQL_CONTAINER[include_sql_id]
                if include_sql_model.includes:
                    raise MapperError("Nested include: '%s' include '%s' and it include %s in mapper file: %s" % (
                        sql_ids[i], include, include_sql_model.includes, file))

    # include sql
    include_results = filter(lambda x: x[1] is not None, results)
    for sql_id, includes in include_results:
        _handle_includes(build_sql_id(namespace, sql_id), includes)

    # dynamic sql change to Template
    for sql_id in sql_ids:
        sql_model = _SQL_CONTAINER[build_sql_id(namespace, sql_id)]
        if sql_model.dynamic:
            sql_model.sql = Template(sql_model.sql)


def _handle_includes(sql_id, includes):
    is_dynamic = False
    sql_model = _SQL_CONTAINER[sql_id]
    for include in includes:
        include_sql_id = build_sql_id(sql_model.namespace, include)
        include_sql_model = _SQL_CONTAINER[include_sql_id]
        if include_sql_model.dynamic:
            is_dynamic = True
        if include_sql_model.includes:
            _handle_includes(include_sql_id, include_sql_model.includes)
        sql = re.sub(r'{{\s*%s\s*}}' % include, include_sql_model.sql, sql_model.sql)

    _valid_sql(sql_id, sql, sql_model.action)
    if is_dynamic or is_dynamic_sql(sql):
        sql_model.dynamic = True
        sql_model.mapping = True
        sql_model.placeholder = False
    else:
        sql_model.mapping = ':' in sql
        sql_model.placeholder = False if sql_model.mapping else '?' in sql
    sql_model.sql = sql
    sql_model.includes = None


def _load_sql(namespace, child, file):
    global _SQL_CONTAINER
    includes = None

    _id = child.attrib.get('id')
    assert _id, "Mapper 'id' must be set in mapper file: %s." % file
    sql_id = build_sql_id(namespace, _id)
    assert sql_id not in _SQL_CONTAINER, "Sql id '%s' repeat." % sql_id
    include = child.attrib.get('include')
    sql = child.text.strip()
    action = child.tag
    pk_seq = child.attrib.get('pkSeq')
    select_key = child.attrib.get('selectKey')
    if include:
        includes = include.split(",")
        for include in set(includes):
            assert include != _id, "Include must not be it self, id: '%s' = include: '%s' " % (_id, include)
        _SQL_CONTAINER[sql_id] = SqlModel(sql=sql, action=action, namespace=namespace, includes=includes, pk_seq=pk_seq, select_key=select_key)
    elif is_dynamic_sql(sql):
        _valid_sql(sql_id, sql, child.tag)
        _SQL_CONTAINER[sql_id] = SqlModel(sql=sql, action=action, namespace=namespace, dynamic=True, pk_seq=pk_seq, select_key=select_key)
    else:
        _valid_sql(sql_id, sql, child.tag)
        _SQL_CONTAINER[sql_id] = SqlModel(sql=sql, action=action, namespace=namespace, pk_seq=pk_seq, select_key=select_key)

    return _id, includes


def _valid_sql(sql_id, sql, tag):
    assert tag in _valid_sql_actions and tag in sql.lower(), "Sql id: '{}' has not '{}' key word in {} sql.".format(sql_id, tag, tag)
