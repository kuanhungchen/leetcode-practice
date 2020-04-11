class MyHashMap:

    def __init__(self):
        self.arr = [-1 for _ in range(10 ** 6)]

    def put(self, key: int, value: int):
        self.arr[key] = value

    def get(self, key):
        return self.arr[key]

    def remove(self, key):
        self.arr[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
