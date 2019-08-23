class Solution:
    def hasGroupsSizeX(self, deck):
        from collections import Counter
        if not deck:
            return False
        _dict = Counter(deck)
        # use collections to replace dictionary
        # faster than dictionary

        def gcd(a, b):
            if a % b == 0:
                return b
            elif b % a == 0:
                return a
            elif a > b:
                return gcd(b, a % b)
            elif b > a:
                return gcd(a, b % a)

        _x = list(_dict.values())[0]

        for k, v in _dict.items():
            _x = gcd(_x, v)
        return _x >= 2
