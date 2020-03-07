class Solution:
    def countNegatives(self, grid):
        ans = 0
        for row in grid:
            for ele in row:
                if ele < 0:
                    ans += 1
        return ans
