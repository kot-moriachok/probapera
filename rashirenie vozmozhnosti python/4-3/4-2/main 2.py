from orm.Сonnection import Connection
from orm.session_builder import SessionBuilder

session = SessionBuilder(
    Connection(
        server='localhost',
        port=5432,
        user='postgres',
        password='123',
        bd_name='synergy',
        sql_type='PostgresSQL'
    )
).buid()