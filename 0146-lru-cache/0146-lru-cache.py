from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache= OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Senior move: move to end on every access
        self.cache.move_to_end(key)
        return self.cache[key]
        
        

    def put(self, key: int, value: int) -> None:
      # If key exists, move it to the end (mark as most recent)
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            # last=False pops the FIFO (Least Recently Used) item
            self.cache.popitem(last=False)
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)