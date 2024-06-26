#!/usr/bin/python3
"""
class LFUCache that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Caching system using LFU strategy.
    """
    def __init__(self):
        """
        Initialize the LFUCache.
        """
        super().__init__()

        # Store the frequencies in a list, each index corresponding to a key
        self.frequencies = []

    def put(self, key, item):
        """
        Add an item in the cache using LFU strategy
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfu = min(self.frequency.values())
                lfu_keys = []
                for k, v in self.frequency.items():
                    if v == lfu:
                        lfu_keys.append(k)
                if len(lfu_keys) > 1:
                    lru_lfu = {}
                    for k in lfu_keys:
                        lru_lfu[k] = self.usage.index(k)
                    discard = min(lru_lfu.values())
                    discard = self.usage[discard]
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usage[self.usage.index(discard)]
                del self.frequency[discard]
            # update usage frequency
            if key is self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.cache_data[key]= item
            self.usage.append(key)

    def get(self, key):
        """
        Return the value linked to a given key, or None.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data.get[key]
        return None
