#!/usr/bin/python3
"""
class LRUCache that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Least recently used cache.
    """
    def __init__(self):
        """
        Initialize.
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Add data to cache and or delete it lru.
        """
        if key is None or item is None:
            pass
        else:
            size = len(self.cache_data)
            if size >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.cache_data[ke] = item
            self.usage.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
