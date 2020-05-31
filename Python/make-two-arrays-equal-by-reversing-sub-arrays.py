class Solution:
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        return target == arr
