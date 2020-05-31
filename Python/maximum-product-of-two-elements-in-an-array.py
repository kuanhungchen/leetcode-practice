class Solution:
    def maxProduct(self, nums):
        mx1 = -1
        i1 = None
        for i, num in enumerate(nums):
            if num > mx1:
                i1 = i
                mx1 = num
        mx2 = -1
        for i, num in enumerate(nums):
            if i == i1:
                continue
            if num > mx2:
                mx2 = num
        return (mx1 - 1) * (mx2 - 1)
