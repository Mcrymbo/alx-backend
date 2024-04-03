#!/usr/bin/env python3
"""
LIFO Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class for LIFOCaching
    """

    def __init__(self):
        """ initialize LIFOCache class """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ adds items to LIFO cache """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.stack:
                discarded = self.stack.pop()
                del self.cache_data[discarded]
                print('DISCARD:', discarded)

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """ return the value of a key in a cache """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
