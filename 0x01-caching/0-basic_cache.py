#!/usr/bin/env python3
'''Basic caching system
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache class inheriting from BaseCaching.
    '''

    def put(self, key, item):
        '''Assign item to self.cache_data using key.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Return value linked to key from self.cache_data.
        '''
        return self.cache_data.get(key)
