class Solution:
    def climbStairs(self, n):
        ans = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for i in range(11, n):
            ans.append(ans[i-1] + ans[i-2])
        return ans[n-1]
