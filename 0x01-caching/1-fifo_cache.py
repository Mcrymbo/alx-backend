#!/usr/bin/env python3
"""
FIFO caching
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ class for FIFO caching """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ adds item to the cache """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)
                print('Discard:', discarded[0])

    def get(self, key):
        """ return the value linked with the key """
        if key in self.cache_data:
            return self.cache_data.get(key)
