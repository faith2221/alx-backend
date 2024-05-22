#!/usr/bin/python3
"""
class BasicCache that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system.
    """
    def __init__(self):
        """
        Initialize.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add data to cache.
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value in self.cache_data linked to a key.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
