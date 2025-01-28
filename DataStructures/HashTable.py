class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size # Lets say size is 10, it will comeup with 10 empty arrays
    
    def hash(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
        else:
            while node:
                if node.key == key: # If same key appears, update its value
                    node.value = value   
                    return             
                if node.next is None: # if node.next is empty, break out of loop
                    break
                node = node.next # If the above 2 conditions is never meet, continue iterating
            node.next = Node(key, value)
        
    def get(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

hash_map = HashMap(10)
hash_map.insert(10, 'A')
hash_map.insert(22, 'B')
hash_map.insert(37, 'C')
hash_map.insert(47, 'D')
hash_map.insert(57, 'E')
hash_map.insert(67, 'F')

print(hash_map.get(67))