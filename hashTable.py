class MyHashMap:

    def __init__(self):
        self.hashTable = [[0 for i in range(0)] for j in range(2069)]

        """
        Initialize your data structure here.

        """
    def hash(self, key: int):
        hash = key % 2069
        return hash


    def put(self, key: int, value: int) -> None:
        hashedKey = hash(key)
        found = False
        for i, kv in enumerate(self.hashTable[hashedKey]):
            if key == kv[0]:
                self.hashTable[hashedKey][i] = (key, value)
                found = True
                break

        if not found:
            self.hashTable[hashedKey].append((key, value))



    def get(self, key: int) -> int:
        hashedKey = hash(key)
        for (k, v) in self.hashTable[hashedKey]:
            if k == key:
                return v
        return -1


    def remove(self, key: int) -> None:
        hashedKey = hash(key)
        for i, kv in enumerate(self.hashTable[hashedKey]):
            if key == kv[0]:
                del self.hashTable[hashedKey][i]

        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

