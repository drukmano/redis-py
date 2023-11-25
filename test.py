import asyncio

url = 'redis://'

from redis.client import Redis as RedisSync
from redis.asyncio.client import Redis as RedisAsync

def sync():
  r = RedisSync.from_url(url)
  print(r.set('123', '1', nx=True, ex=10))
  print(r.ttl('123'))

async def async_():
  r = RedisAsync.from_url(url)
  print(await r.set('123', '1', nx=True, ex=10))
  print(await r.ttl('123'))
  await r.aclose()


sync()
asyncio.run(async_())
