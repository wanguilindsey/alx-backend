#!/usr/bin/env python3
"""LIFO caching system.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache system using OrderedDict.
    """
    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item to cache with LIFO eviction if needed.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", last_key)
        self.cache_data[key] = item

    def get(self, key):
        """Get item from cache by key.
        """
        return self.cache_data.get(key)
