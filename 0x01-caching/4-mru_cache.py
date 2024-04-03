#!/usr/bin/env python3
"""
LRU Caching policy
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ class for LRUCache """

    def __init__(self):
        """ initialize LRU cache class """
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru = ''

    def put(self, key, item):
        """ adds item to LRUCache """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.mru = key
                else:
                    discarded = self.mru
                    del self.cache_data[discarded]
                    print('DISCARD:', discarded)
                    self.cache_data[key] = item
                    self.mru = key
            else:
                self.cache_data[key] = item
                self.mru = key

    def get(self, key):
        """ return the value of cache_data linked to key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
