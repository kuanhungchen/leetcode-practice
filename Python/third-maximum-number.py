class Solution:
    def thirdMax(self, nums):
        mx1, mx2, mx3 = -10**15, -10**15, -10**15
        for num in nums:
            if num in [mx1, mx2, mx3]:
                continue
            if num > mx1:
                mx1, mx2, mx3 = num, mx1, mx2
            elif num > mx2:
                mx2, mx3 = num, mx2
            elif num > mx3:
                mx3 = num
        return mx3 if mx3 > -10**15 else mx1
