#!/usr/bin/env python3
""" Cache class """
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Cache class to write strings to Redis"""
    def __init__(self):
        """Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method genrates a random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        """Convert the data back to the desired format"""
        val = self._redis.get(key)
        if val is None:
            return None
        if fn:
            return fn(val)
        return val

    def get_str(self, key):
        """Automatically parametrize Cache.get to str"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        """Automatically parametrize Cache.get to int"""
        return self.get(key, fn=int)
