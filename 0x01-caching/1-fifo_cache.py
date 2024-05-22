#!/usr/bin/python3
"""
class FIFOCache that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First in First out cache.
    """
    def __init__(self):
        """
        Initialize.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add data to cache or delete it.
        """
        if key is None or item is None:
            pass
        else:
            size = len(self.cache_data)
            if size >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                print('DISCARD: {}'.format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
