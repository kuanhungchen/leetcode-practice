class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.pre = None
        self.nxt = None


class LRUCache:

    def __init__(self, cap):
        self.mp = dict()
        self.cap = cap
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def get(self, key):
        if key not in self.mp:
            return -1
        n = self.mp[key]
        self._remove(n)
        self._add(n)
        return n.v

    def put(self, key, value):
        if key in self.mp:
            n = self.mp[key]
            self._remove(n)
        n = Node(key, value)
        self._add(n)
        self.mp[key] = n
        if len(self.mp) > self.cap:
            n = self.head.nxt
            self._remove(n)
            del self.mp[n.k]

    def _add(self, node):
        p = self.tail.pre
        p.nxt = node
        self.tail.pre = node
        node.pre = p
        node.nxt = self.tail

    def _remove(self, node):
        p = node.pre
        n = node.nxt
        p.nxt = n
        n.pre = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
