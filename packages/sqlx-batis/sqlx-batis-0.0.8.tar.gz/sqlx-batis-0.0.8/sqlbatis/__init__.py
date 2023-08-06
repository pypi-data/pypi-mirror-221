from sqlexec import (
    connection,
    transaction,
    with_connection,
    with_transaction,
    get_connection,
    Engin,
    DBEngin
)
from .sql_mapper import sql, mapper
from .snowflake import init_snowflake, get_snowflake_id

def init_db(host='127.0.0.1', port=3306, database='test', user='root', password='', mapper_path='mapper', engin=Engin.MYSQL, pool_size=0, show_sql=False, **kwargs):
    from .sql_holder import load_mapper
    from sqlexec import init_db as supper_init_db
    load_mapper(mapper_path)
    supper_init_db(host=host, port=port, user=user, database=database, password=password, engin=engin, pool_size=pool_size, show_sql=show_sql, **kwargs)
