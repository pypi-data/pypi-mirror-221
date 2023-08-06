from sqlexec import (
    connection,
    transaction,
    with_connection,
    with_transaction,
    get_connection,
    DBError
)
from .engine import Engine
from .sql_mapper import sql, mapper
from .snowflake import init_snowflake, get_snowflake_id

def init_db(driver='', mapper_path='mapper', pool_size=0, show_sql=False, debug=False,  **kwargs):
    from .sql_holder import load_mapper
    from sqlexec import init_db as supper_init_db
    Engine.init()
    supper_init_db(driver=driver, pool_size=pool_size, show_sql=show_sql,debug=debug, **kwargs)
    load_mapper(mapper_path)


