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
