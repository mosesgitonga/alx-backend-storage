#!/usr/bin/env python3
"""
creating a simple cache
"""
import redis
import uuid
from typing import List, Union


class Cache:
    """
    writing strings to redis
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
