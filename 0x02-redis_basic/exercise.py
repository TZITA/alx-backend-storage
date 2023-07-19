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
        return self._redis.get(key)

    def get_str(self):
        """Automatically parametrize Cache.get to str"""
        return str(self.get())

    def get_int(self):
        """Automatically parametrize Cache.get to int"""
        return int(self.get())
