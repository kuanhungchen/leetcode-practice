class Solution:
    def createTargetArray(self, nums, index):
        target = []
        for n, i in zip(nums, index):
            target.insert(i, n)
        return target
