class Solution:
    def isMonotonic(self, A):
        if len(A) < 3:
            return True
        a = sorted(A)
        b = a[::-1]
        return A == a or A == b
