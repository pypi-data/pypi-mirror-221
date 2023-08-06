from sqlbatis import (
    connection,
    transaction,
    with_connection,
    with_transaction,
    get_connection,
    init_snowflake,
    get_snowflake_id,
)
from .sql_mapper import sql, mapper

def init_db(host='127.0.0.1', port=3306, database='test', user='root', password='', mapper_path='mapper', pool_size=0, show_sql=False, **kwargs):
    from .engin import PostgresEngin
    from sqlbatis import init_db as supper_init_db
    supper_init_db(host=host, port=port, user=user, database=database, password=password, mapper_path=mapper_path, pool_size=pool_size, \
                   show_sql=show_sql, **kwargs)
    PostgresEngin.init()
