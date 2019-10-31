class Solution:
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            # x^0 = x
            # x^x = 0
            # (x^y)^x = y
            # (x^y)^y = x
            ans ^= num
        return ans
