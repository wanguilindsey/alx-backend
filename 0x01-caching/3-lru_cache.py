#!/usr/bin/env python3
'''LRU caching system
'''

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''LRU cache system using OrderedDict.
    '''

    def __init__(self):
        '''Initialize the cache.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Add item to cache with LRU eviction if needed.
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        '''Get item from cache by key and update usage.
        '''
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
