from collections import Counter
class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.LFUValue = {}
        self.LFUTime = Counter()
        self.LFUCalled = {}
        self.time = 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not self.capacity:
            return -1
        
        self.time += 1
        val = self.LFUValue.get(key)

        if val == None:
            return -1

        self.LFUTime[key] += 1
        self.LFUCalled[key] = self.time
        return val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.time += 1
        if not self.capacity:
            return

        if key in self.LFUValue:
            self.LFUValue[key] = value
            self.LFUTime[key] += 1
            self.LFUCalled[key] = self.time
        else:
            if len(self.LFUTime) < self.capacity:
                self.LFUValue[key] = value
                self.LFUTime[key] = 1
                self.LFUCalled[key] = self.time
            else:
                leastFrequency = min(self.LFUTime.values())
                valueToPop = float('inf')
                keyToPop = 0
                for i in self.LFUTime:
                    if self.LFUTime[i] == leastFrequency:
                        if valueToPop > self.LFUCalled[i]:
                            keyToPop = i
                            valueToPop = self.LFUCalled[i]
                self.LFUValue.pop(keyToPop)
                self.LFUCalled.pop(keyToPop)
                self.LFUTime.pop(keyToPop)
                
                self.LFUValue[key] = value
                self.LFUTime[key] += 1
                self.LFUCalled[key] = self.time

# Your LFUCache object will be instantiated and called as such:
cache = LFUCache(1);


cache.put(0, 0);
print cache.get(0);
# print cache.get(1);       # returns 1
# cache.put(3, 3);   
# print cache.get(2);       # returns -1 (not found)
# print cache.get(3);       # returns 3.
# cache.put(4, 4);    # evicts key 1.
# print cache.get(1);       # returns -1 (not found)
# print cache.get(3);       # returns 3
# print cache.get(4);       # returns 4