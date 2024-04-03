#!/usr/bin/env python3
"""
LRU Caching policy
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ class for LRUCache """

    def __init__(self):
        """ initialize LRU cache class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ adds item to LRUCache """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)
                print('DISCARD:', discarded[0])

    def get(self, key):
        """ return the value of cache_data linked to key """
        if key is None or key not in self.cache_data.keys():
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
