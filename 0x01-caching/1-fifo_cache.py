#!/usr/bin/env python3
"""
FIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ class for FIFO caching """
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ adds item to the cache """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.queue:
                    discarded = self.queue.pop(0)
                    del self.cache_data[discarded]
                    print('Discard:', discarded)

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ return the value linked with the key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
