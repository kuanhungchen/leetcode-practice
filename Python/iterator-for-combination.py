class CombinationIterator:

    def __init__(self, chars, length):
        self.len = len(chars)
        self.chars = chars
        self.pointers = [i for i in range(length)]
        self.pointers[-1] -= 1
        self.thres = [i for i in range(self.len - len(self.pointers), self.len)]

    def next(self):
        idx = 1
        while self.pointers[-idx] + idx >= self.len:
            idx += 1

        self.pointers[-idx] += 1
        idx -= 1
        while idx != 0:
            self.pointers[-idx] = self.pointers[-idx - 1] + 1
            idx -= 1

        ans = ""
        for p in self.pointers:
            ans += self.chars[p]

        return ans

    def hasNext(self):
        return self.pointers != self.thres

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

