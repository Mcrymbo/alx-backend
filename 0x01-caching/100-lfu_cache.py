#!/usr/bin/env python3
"""
Implements LFUCache
"""
from collections import OrderedDict, defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ class that implements LFU caching policy """

    def __init__(self):
        """ i itialize LFUCache class """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        ''' add item to a LFUCache '''

        if key and item:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_freq = min(self.frequency.values())
                    min_freq_used = [k for k, v in self.frequency.items() if v == min_freq]

                    for k in min_freq_used:
                        del self.cache_data[k]
                        print('DISCARD:', k)
                        del self.frequency[k]
                        break

                self.cache_data[key] = item
                self.frequency[key] = 1
    
    def get(self, key):
        """ get a cached data based on a key """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.frequency[key] += 1
            return self.cache_data.get(key)
