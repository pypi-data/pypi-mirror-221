from sqlbatis import (
    connection,
    transaction,
    with_connection,
    with_transaction,
    get_connection,
    init_snowflake,
    get_snowflake_id
)

from .sql_mapper import sql, mapper
from sqlbatis.engine import PostgresEngine

def init_db(mapper_path='./mapper', pool_size=0, show_sql=False, **kwargs):
    from sqlbatis import init_db as supper_init_db

    PostgresEngine.init()
    supper_init_db(mapper_path=mapper_path, pool_size=pool_size, show_sql=show_sql, **kwargs)

