#!/usr/bin/env python3
"""
creating a simple cache
"""
import redis
import uuid
from typing import List, Union, Callable, Optional
from functools import wraps


class Cache:
    """
    writing strings to redis
    """
    def __init__(self):
        """
        instatiate
        """
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()
        self.calls_counter = {}

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(cls, *args, **kwargs):
            key = method.__qualname__
            cls.calls_counter[key] = cls.calls_counter.get(key, 0) + 1
            result = method(cls, *args, **kwargs)
            return result
        return wrapper

    @count_calls
    def store(self, data: Union[str, int, bytes, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, bytes]]] = None) -> Union[str, int, bytes, None]:
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)
