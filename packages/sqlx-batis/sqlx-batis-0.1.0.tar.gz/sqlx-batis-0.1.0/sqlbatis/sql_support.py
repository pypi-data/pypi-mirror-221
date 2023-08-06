import re
from jinja2 import Template
from functools import lru_cache
from .support import MapperError
from .constant import LIMIT_1, DYNAMIC_REGEX, CACHE_SIZE

# Don't remove. Import for not repetitive implementation
from sqlexec.sql_support import get_named_args, get_named_sql, get_batch_args


def simple_sql(sql: str, *args, **kwargs):
    return get_named_sql_args(sql, **kwargs) if kwargs else (sql, args)


def dynamic_sql(sql: str, *args, **kwargs):
    sql_type = _get_sql_type(sql)
    if sql_type >= 1 and not kwargs:
        raise MapperError("Parameter 'kwargs' must not be empty when named mapping sql.")
    if sql_type == 0:
        return sql, args
    if sql_type == 1:
        sql = Template(sql).render(**kwargs)
    return get_named_sql_args(sql, **kwargs)


def get_page_start(page_num: int, page_size: int):
    assert page_num >= 1 and page_size >= 1, "'page_name' and 'page_size' should be higher or equal to 1"
    return (page_num - 1) * page_size


def limit_one_sql_args(sql: str, *args):
    if require_limit(sql):
        return '{} LIMIT ?'.format(sql), [*args, LIMIT_1]
    return sql, args


def is_dynamic_sql(sql: str):
    return re.search(DYNAMIC_REGEX, sql)


def get_named_sql_args(sql: str, **kwargs):
    args = get_named_args(sql, **kwargs)
    return get_named_sql(sql), args


def require_limit(sql: str):
    lower_sql = sql.lower()
    if 'limit' not in lower_sql:
        return True
    idx = lower_sql.rindex('limit')
    if idx > 0 and ')' in lower_sql[idx:]:
        return True
    return False


@lru_cache(maxsize=2*CACHE_SIZE)
def _get_sql_type(sql: str):
    """
    :return: 0: placeholder, 1: dynamic, 2: named mapping
    """
    if is_dynamic_sql(sql):
        return 1
    if ':' in sql:
        return 2
    return 0

