#!/usr/bin/env python3
"""
creating a simple cache
"""
import redis
import uuid
from typing import List, Union, Callable, Optional
from functools import wraps


def replay(method: Callable) -> None:
    """
    displays the history of calls made by a particular method by retrieving
    the inputs and outputs saved on the redis store
    """
    meth_name = method.__qualname__
    redis_db = method.__self__._redis
    inputs = redis_db.lrange(meth_name + ":inputs", 0, -1)
    outputs = redis_db.lrange(meth_name + ":outputs", 0, -1)

    print(f"{meth_name} was called {len(inputs)} times:")
    for input, output in zip(inputs, outputs):
        input = input.decode("utf-8")
        output = output.decode("utf-8")
        print(f"{meth_name}(*{input}) -> {output}")


def call_history(method: Callable) -> Callable:
    """
    decorates a method to record its input output history
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        meth_name = method.__qualname__
        self._redis.rpush(meth_name + ":inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(meth_name + ":outputs", output)
        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


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

    @call_history
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
