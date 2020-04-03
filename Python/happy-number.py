class Solution:
    def isHappy(self, n):
        cache = set()
        while n not in cache:
            cache.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
            if n == 1:
                return True
        return False
