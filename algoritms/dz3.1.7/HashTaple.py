class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash_function(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        # обновление значения, если ключ уже есть
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return

    def resize(self):
        new_size = self.size * 2
        new_table = [None] * new_size
        old_table = self.table
        self.size = new_size
        self.table = new_table
        for bucket in old_table:
            if bucket:
                for k, v in bucket:
                    index = hash_function(k) % self.size
                    if self.table[index] is None:
                        self.table[index] = []
                    self.table[index].append((k, v))
def hash_function(s):
    total = 0
    for char in s:
        total += ord(char)
    return total

hash_map = {}

def add_element(key):
    hash_value = hash_function(key)
    hash_map[key] = hash_value

def get_hashed_value(key):
    return hash_map.get(key)


ht = HashTable()
for i in range(10):
    ht.insert(f"key{i}", i)

print("Поиск:", ht.search("key5"))  # должно вернуть 5
ht.delete("key5")
print("После удаления:", ht.search("key5"))  # должно вернуть None
ht.resize()

# Работа с словарём и функцией-хешем
add_element("apple")
add_element("banana")
print(get_hashed_value("apple"))  # вывод хеша строки "apple"
print(get_hashed_value("banana"))