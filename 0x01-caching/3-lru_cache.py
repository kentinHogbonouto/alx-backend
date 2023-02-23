#!/usr/bin/env python3
"""
Caching class that inherits from the base class, BaseCashing
Has limited cashing capabilities
Implements the LRU caching algorithim
"""
import sys
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Caching class that inherits from the base class, BaseCashing
    Has limited cashing capabilities (limited space)
    Implements the LRU caching algorithim
    """
    def __init__(self) -> None:
        """
        Creates the dictionary and list object
        """
        super().__init__()
        self.age_dict = {}
        self.counter = 0

    def put(self, key, item):
        """
        Method that populates the cache given a key and item
        The LRU caching algorithim is used to populate the
        cache
        """
        if key is None or item is None:
            return
        # Checking if the key exists in the
        # dictionary, and performing an insert
        # into the actual dictionary and age
        # tracking dictionary
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.age_dict[key] = self.counter
            self.counter += 1
        else:
            # Checking if the cache limit has reached
            if (len(self.cache_data) == BaseCaching.MAX_ITEMS):
                # Get the key (k) with the smallest age
                # , the least recently used key, this is
                # done by sorting the dictionary by age
                min_age_value = sys.maxsize
                min_age_key = None
                for k, age in self.age_dict.items():
                    if age < min_age_value:
                        min_age_value = age
                        min_age_key = k

                # Remove the key with minimum age from the
                # actual dictionary and age_dictinary
                self.cache_data.pop(min_age_key)
                print("DISCARD: {}".format(min_age_key))
                self.age_dict.pop(min_age_key)
            # Inserting the new key and item, while also
            # assigning it an age
            self.cache_data[key] = item
            # print("In here ",key, item)
            self.age_dict[key] = self.counter
            self.counter += 1

    def get(self, key):
        """
        Method that retrieves the data from the cache given
        the key
        """
        value = self.cache_data.get(key, None)
        if value is not None:
            # Updating the age of the key
            self.age_dict[key] = self.counter
            self.counter += 1
        return value
