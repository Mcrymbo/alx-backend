#!/usr/bin/env python3
"""
Module that implements basic caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    a class that implements basic dictionary catching
    """
    def put(self, key, item):
        """ add an item in the cache """
        if not key or not item:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ get an item by the key """
        if not key or key not in self.cache_data.keys():
            return None

        return self.cache_data.get(key)
