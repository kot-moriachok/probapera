import api.users.get as users_get
from redis import asyncio as aioredis
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache import FastAPICache

from fastapi import FastAPI
app = FastAPI()

@app.on_event('startup')
async def startup_event():
     redis = aioredis.from_url('redis://localhost', encoding='utf-8',decode_responses=True)
     fastapicache.init(RedisBackend(redis), prefix='fastapi-cache')
app.include_router(users_get.router, tags=['users'], prefix='/users')
