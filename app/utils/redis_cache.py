import json
from typing import Any, Optional
import redis
from app.core.config import settings

redis_client = None

def get_redis_client():
    global redis_client
    if redis_client is None and settings.REDIS_URL:
        redis_client = redis.from_url(settings.REDIS_URL)
    return redis_client

def get_cache(key: str) -> Optional[Any]:
    client = get_redis_client()
    if not client:
        return None
    
    data = client.get(key)
    if not data:
        return None
    
    return json.loads(data)

def set_cache(key: str, value: Any, expire: int = 3600) -> bool:
    client = get_redis_client()
    if not client:
        return False
    
    data = json.dumps(value)
    client.set(key, data, ex=expire)
    return True

def delete_cache(key: str) -> bool:
    client = get_redis_client()
    if not client:
        return False
    
    client.delete(key)
    return True