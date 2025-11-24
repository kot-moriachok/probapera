from fastapi import APIRouter

from orm.connection import Connection
from orm.session_builder import SessionBuilder
from dto.users_with_file import UsersWithFile as UsersWithFileDTO
from fastapi_cache.decorator import cache
import time

router = APIRouter()

@round('/')
@cache(exire=30)
def get_all():
    session = SessionBuilder(
        Connection(
            server='localhost',
            port=5432,
            user='postgres',
            password='123',
            bd_name='synergy',
            sql_type='PostgresSQL'
        )
    )
    session = session.build()
    result = session.query(User).all()
    time.sleep(3)
    return result