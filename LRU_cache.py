class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    # @return an integer
    def get(self, key):
        if key in self.cache:
            return self.cache[key][1]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # self.cache[key][0] starts with 1;
        if key in self.cache:
            self.cache[key][1] = value
            pivot = self.cache[key][0]
            for _key in self.cache:
                if _key != key and self.cache[_key][0] > pivot:
                    self.cache[_key][0] -= 1
            self.cache[key][0] = len(self.cache)
        else:
            # if cache is full:
            if len(self.cache) == self.capacity:
                key_deleted = None
                for _key in self.cache:
                    if self.cache[_key][0] == 1:  # The least recently used;
                        key_deleted = _key
                    else:
                        self.cache[_key][0] -= 1
                del self.cache[key_deleted]
                self.cache[key] = [self.capacity, value]
            # or cache is not full:
            else:
                self.cache[key] = [len(self.cache) + 1, value]

    def print_cache(self):
        for key in self.cache:
            print key, self.cache[key]
        print "\n"

if __name__ == "__main__":
    solution = LRUCache(4)
    solution.set(1, 10)
    solution.print_cache()
    solution.set(2, 20)
    solution.print_cache()
    solution.set(3, 30)
    solution.print_cache()
    solution.set(4, 40)
    solution.print_cache()
    solution.set(5, 55)
    solution.print_cache()
    solution.set(2, 21)
    solution.print_cache()
    print solution.get(5)
    print solution.get(8)

# The algorithm is used to simulate the mechanism of LRU cache. It's basic principle is:
# 1. if the key (tag) is in the cache, get it;
# 2. if the key is not in the cache:
#    1. if the cache is not full, write data into cache from memory and set it as the most recently used;
#    2. if the cache is full, find the least recently used and rewrite it, then set it as the most recently used;