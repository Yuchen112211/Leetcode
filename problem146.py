'''

146. LRU Cache
Medium

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

 
Solution:
Use list, actually it's better to use deque and appendleft.
Use insert(0,x) in list is more time complexity and space complexity.
Nothing hard, the key is in get function we need to delete the given key then insert
it into the head of the list/deque.

In put function, we need to determine whether the cache has reached its size, then to
pop out or modify.
'''


class LRUCache(object):
    def __init__(self, capacity):
        self.time_LRU = []
        self.pos_LRU = {}
        self.capacity = capacity

    def get(self, key):
        if key in self.pos_LRU:
            self.time_LRU.remove(key)
            self.time_LRU.insert(0,key)
            return self.pos_LRU[key]
        else:
            return -1

    def put(self, key, value):
        if key not in self.pos_LRU and len(self.pos_LRU) == self.capacity:
            to_delete_key = self.time_LRU.pop()
            tmp = self.pos_LRU.pop(to_delete_key)
        elif key in self.pos_LRU:
            self.time_LRU.remove(key)
        self.time_LRU.insert(0,key)
        self.pos_LRU[key] = value

if __name__ == '__main__':
    obj = LRUCache(2)
    print obj.get(2)
    obj.put(2,6)
    print obj.get(1)
    obj.put(1,5)
    obj.put(1,2)
    print obj.get(1)
    print obj.get(2)
