'''
Runtime analysis:

Average case runtime of lookup in dict is O(1) same goes for adding item to dict().
OrderedDict moves items in constant time too. Hence all operations performed here are constant time.

'''

from collections import deque, OrderedDict
from typing import Any

class LRU_Cache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.hmap: 'OrderedDict[int, Any]' = OrderedDict()

    def get(self, key: int) -> Any:
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.hmap:
            self.hmap.move_to_end(key, last=False)
            return self.hmap[key]
        return -1

    def set(self, key: int, value: Any) -> None:
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.hmap:
            if len(self.hmap) >= self.capacity:
                self.hmap.popitem()
            self.hmap[key] = value
            self.hmap.move_to_end(key, last=False)


if __name__ == "__main__":
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)


    assert our_cache.get(1) == 1       # returns 1
    assert our_cache.get(2) == 2       # returns 2
    assert our_cache.get(9) == -1      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    assert our_cache.get(3) == -1      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry