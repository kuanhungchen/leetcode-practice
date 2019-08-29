class Solution:
    def mySqrt(self, x):
        # use binary search, else it would be TLE
        if x < 2:
            return x
        left = 0
        right = x
        num = (right + left) // 2
        while True:
            if num * num <= x < (num+1) * (num+1):
                return num
            elif x < num * num:
                right = num
                num = (right + left) // 2
            else:
                left = num
                num = (right + left) // 2
