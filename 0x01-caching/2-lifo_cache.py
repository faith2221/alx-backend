#!/usr/bin/python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Last in First out cache.
    """
    def __init__(self):
        """
        Initialize.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add data to cache or delete it.
        """
        if key is None or item is None:
            pass
        else:
            size = len(self.cache_data)
            if size >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data.keys():
            return self.cache_data.(key)
        return None
