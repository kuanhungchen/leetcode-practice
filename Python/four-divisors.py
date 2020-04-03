class Solution:
    def sumFourDivisors(self, nums):
        def solve(x):
            cnt, sm = 0, 0
            for div in range(1, int(x ** 0.5) + 1):
                if not (x % div):
                    cnt += 1
                    sm += div
                    if div * div != x:
                        cnt += 1
                        sm += x // div
            return cnt, sm

        ans = 0
        for num in nums:
            c, s = solve(num)
            if c == 4:
                ans += s
        return ans
