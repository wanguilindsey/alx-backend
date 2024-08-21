#!/usr/bin/env python3
'''FIFO caching system
'''

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO cache system using OrderedDict.
    '''

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Add item to cache with FIFO eviction if needed.
        '''
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''Get item from cache by key.
        '''
        return self.cache_data.get(key)
