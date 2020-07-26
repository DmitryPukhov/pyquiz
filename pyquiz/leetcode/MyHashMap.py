class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nbuckets = 10000
        self.buckets = [[]] * self.nbuckets

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = self.buckets[key % self.nbuckets]
        flag = False
        for i in range(0, len(bucket)):
            k, v = bucket[i]
            if k == key:
                bucket[i] = (key,value)
                flag = True
                break
        if not flag:
            bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = self.buckets[key % self.nbuckets]
        for k,v in bucket:
            if k == key: return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.buckets[key % self.nbuckets] = list(filter(lambda t: t[0]!=key, self.buckets[key % self.nbuckets]))

    # Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
