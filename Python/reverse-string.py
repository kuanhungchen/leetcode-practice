class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = [s[len(s) - 1- i] for i in range(len(s))]
