import re
from sqlexec import get
from typing import Sequence
from .support import DBError
from functools import lru_cache
from .log_support import logger
from sqlexec.engin import Engin as BaseEngin
from .sql_support import require_limit, get_page_start
from .constant import MYSQL_COLUMN_SQL, POSTGRES_COLUMN_SQL, MYSQL_SELECT_KEY, LIMIT_1, MYSQL, POSTGRESQL, DEFAULT_KEY_FIELD, CACHE_SIZE


# Engin = Enum('Engin', ['MYSQL', 'POSTGRESQL', 'OTHER'])
# class Engin(Enum):
#     MYSQL = 'MySQL'
#     POSTGRESQL = 'PostgreSQL'
#     OTHER = 'Other'


class Engin(BaseEngin):
    def __init__(self, name=None):
        super().__init__(name)

    @staticmethod
    def get_page_sql_args(sql: str, page_num: int, page_size: int, *args):
        if Engin.current_engin() == MYSQL:
            return MySqlEngin.get_page_sql_args(sql, page_num, page_size, *args)
        elif Engin.current_engin() == POSTGRESQL:
            return PostgresEngin.get_page_sql_args(sql, page_num, page_size, *args)
        raise NotImplementedError(f"Not implement method 'get_page_sql_args' for {Engin.current_engin()}.")

    @staticmethod
    def get_select_key(*args, **kwargs):
        if Engin.current_engin() == MYSQL:
            return MySqlEngin.get_select_key()
        elif Engin.current_engin() == POSTGRESQL:
            return PostgresEngin.get_select_key(*args, **kwargs)
        raise NotImplementedError(f"Not implement method 'get_select_key' for {Engin.current_engin()}.")

    @staticmethod
    def get_table_columns(table: str):
        if Engin.current_engin() == MYSQL:
            return MySqlEngin.get_table_columns(table)
        elif Engin.current_engin() == POSTGRESQL:
            return PostgresEngin.get_table_columns(table)
        raise "*"



class MySqlEngin(Engin):
    def __init__(self, engin):
        super().__init__(engin)

    @classmethod
    def init(cls, name=MYSQL):
        super().init(name)

    @staticmethod
    def create_insert_sql(table: str, cols: Sequence[str]):
        columns, placeholders = zip(*[('`{}`'.format(col), '?') for col in cols])
        return 'INSERT INTO `{}`({}) VALUES({})'.format(table, ','.join(columns), ','.join(placeholders))

    @staticmethod
    def get_page_sql_args(sql: str, page_num: int, page_size: int, *args):
        start = get_page_start(page_num, page_size)
        if require_limit(sql):
            sql = '{} LIMIT ?, ?'.format(sql)
        args = [*args, start, page_size]
        return sql, args

    @staticmethod
    def get_table_columns(table: str):
        return get(MYSQL_COLUMN_SQL, table, LIMIT_1)

    @staticmethod
    def get_select_key():
        return MYSQL_SELECT_KEY

class PostgresEngin(Engin):
    def __init__(self, engin):
        super().__init__(engin)

    @classmethod
    def init(cls, name=POSTGRESQL):
        super().init(name)

    @staticmethod
    def get_page_sql_args(sql: str, page_num: int, page_size: int, *args):
        start = get_page_start(page_num, page_size)
        if require_limit(sql):
            sql = '{} LIMIT ? OFFSET ?'.format(sql)
        args = [*args, page_size, start]
        return sql, args

    @staticmethod
    def get_table_columns(table: str):
        return get(POSTGRES_COLUMN_SQL, table, LIMIT_1)

    @staticmethod
    def get_select_key(key_seq: str = None, table: str = None, key: str =None, sql: str = None):
        if not key_seq:
            if table:
                key_seq = PostgresEngin.build_key_seq(table, key)
            else:
                if sql:
                    key_seq = PostgresEngin._get_key_seq_from_sql(sql)
                else:
                    raise DBError("Get PostgreSQL select key fail, all of 'key_seq', 'table', 'sql' are None")
        return f"SELECT currval('{key_seq}')"

    @staticmethod
    def build_key_seq(table: str, key: str = None):
        if not key:
            key = DEFAULT_KEY_FIELD
        return f'{table}_{key}_seq'

    @staticmethod
    @lru_cache(maxsize=CACHE_SIZE)
    def _get_key_seq_from_sql(sql: str):
        table = re.search('(?<=into )\w+', sql, re.I)
        key_seq = PostgresEngin.build_key_seq(table.group())
        logger.warning("'key_seq' is None, will use default '{}' from sql.".format(key_seq))
        return key_seq
