# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):pass


class Solution:
    # iterative
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution2:
    # recursive
    def firstBadVersion(self, n):
        left, right = 1, n
        return self.recursive(left, right)

    def recursive(self, l, r):
        if l == r:
            return l
        m = (l+r) // 2
        if isBadVersion(m):
            return self.recursive(l, m)
        else:
            return self.recursive(m+1, r)
