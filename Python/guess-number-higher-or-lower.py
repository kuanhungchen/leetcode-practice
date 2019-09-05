# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num): pass


class Solution(object):
    # recursive
    def guessNumber(self, n):
        return self.recursive(1, n)

    def recursive(self, l, r):
        m = (l+r) // 2
        result = guess(m)
        if result == 0:
            return m
        elif result == -1:
            return self.recursive(l, m)
        elif result == 1:
            return self.recursive(m+1, r)


class Solution2(object):
    # iterative
    def guessNumber(self, n):
        left, right = 1, n
        while True:
            m = (left+right) // 2
            result = guess(m)
            if result == 0:
                return m
            elif result == -1:
                right = m
            elif result == 1:
                left = m + 1