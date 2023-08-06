import re
from .db import do_get
from typing import Sequence
from .support import DBError
from functools import lru_cache
from .log_support import logger
from sqlexec.engin import Engin as BaseEngin
from .constant import CACHE_SIZE, MYSQL_COLUMN_SQL, POSTGRES_COLUMN_SQL, MYSQL_SELECT_KEY, LIMIT_1


# Engin = Enum('Engin', ['MYSQL', 'POSTGRESQL', 'OTHER'])
# class Engin(Enum):
#     MYSQL = 'MySQL'
#     POSTGRESQL = 'PostgreSQL'
#     OTHER = 'Other'


class Engin(BaseEngin):
    def __init__(self, name=None):
        super().__init__(name)

    @staticmethod
    def _page_sql_args(require_limit, sql: str, start, page_size, *args):
        raise NotImplementedError(f"Not implement for {Engin.current_engin()}.")

    @staticmethod
    def _get_select_key(*args, **kwargs):
        if Engin.current_engin() == 'MySQL':
            return MYSQL_SELECT_KEY
        raise DBError(f"Expect 'select_key' but not. you can set it in mapper file with 'selectKey', or in model class with '__select_key__', or @mapper and @sql function with 'select_key'")

    @staticmethod
    def _get_table_columns(table: str):
        if Engin.current_engin() == 'MySQL':
            return do_get(MYSQL_COLUMN_SQL, table, LIMIT_1)
        elif Engin.current_engin() == 'PostgreSQL':
            return do_get(POSTGRES_COLUMN_SQL, table, LIMIT_1)
        raise "*"

