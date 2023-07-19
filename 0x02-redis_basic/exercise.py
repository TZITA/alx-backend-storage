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
