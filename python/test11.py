class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(ch) for ch in key)

    def add(self, key, value):
        index = self.hash(key)
        if index not in self.collection:
            self.collection[index] = {}
        self.collection[index][key] = value

    def lookup(self, key):
        index = self.hash(key)
        return self.collection.get(index, {}).get(key)

    def remove(self, key):
        index = self.hash(key)
        bucket = self.collection.get(index)
        if bucket is not None and key in bucket:
            del bucket[key]
            if not bucket:
                del self.collection[index]