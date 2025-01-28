class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size
    
    def hash(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        while self.buckets[index] is not None:
            if self.buckets[index][0] == value:
                self.buckets[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.buckets[index] = (key, value)
        
    def get(self, key):
        index = self.hash(key)
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                return self.buckets[1]
            index = (index + 1) % self.size
        return None

hash_map = HashMap(10)
hash_map.insert(10, 'A')
hash_map.insert(22, 'B')
hash_map.insert(37, 'C')
hash_map.insert(47, 'D')
hash_map.insert(57, 'E')
hash_map.insert(67, 'F')

print(hash_map.get(67))