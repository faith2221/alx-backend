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
        self.order = []

    def put(self, key, item):
        """
        Add data to cache and or delete it lru.
        """
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
