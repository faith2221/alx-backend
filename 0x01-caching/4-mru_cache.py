#!/usr/bin/python3
"""
class MRUCache that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Most recently used cache.
    """
    def __init__(self):
        """
        Initialize.
        """
        super().__init__()
        self.used_Key = []

    def put(self, key, item):
        """
        Add data to cache and or delete it mru.
        """
        if key is None or item is None:
            pass
        else:
            if key not in self.used_Key:
                self.used_Key.append(key)
            else:
                self.used_Key.append(
                    self.used_Key.pop(self.used_Key.index(key)))
            size = len(self.cache_data)
            if size >= BaseCaching.MAX_ITEMS:
                discard_key = self.used_Key.pop(0)
                self.cache_data.pop(discard_key)
                print('DISCARD: {}'.format(discard_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is not None and key in sself.cache_data.keys():
            self.used_Key.append(self.used_Key.pop(self.used_Key.index(key)))
            return self.cache_data.get(key)
        return None
