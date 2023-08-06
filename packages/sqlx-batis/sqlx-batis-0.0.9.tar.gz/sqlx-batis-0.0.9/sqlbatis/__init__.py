from sqlexec import (
    connection,
    transaction,
    with_connection,
    with_transaction,
    get_connection,
    DBError
)
from .engin import Engin
from .sql_mapper import sql, mapper
from .snowflake import init_snowflake, get_snowflake_id

def init_db(host='127.0.0.1', port=3306, database='test', user='root', password='', driver='', mapper_path='mapper', pool_size=0, show_sql=False, \
        debug=False,  **kwargs):
    from .sql_holder import load_mapper
    from sqlexec import init_db as supper_init_db
    Engin.init()
    supper_init_db(host=host, port=port, database=database, user=user, password=password, driver=driver, pool_size=pool_size, show_sql=show_sql,\
                   debug=debug, **kwargs)
    load_mapper(mapper_path)


