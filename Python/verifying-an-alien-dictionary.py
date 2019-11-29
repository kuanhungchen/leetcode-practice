class Solution:
    def isAlienSorted(self, words, order):
        for i in range(20):
            tmp = [-1 if len(word) <= i else order.index(word[i]) for word in words]
            if tmp != sorted(tmp): return False
            if tmp == sorted(tmp) and len(tmp) == len(set(tmp)): return True
        return True
