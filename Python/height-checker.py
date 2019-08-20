class Solution:
    def heightChecker(self, heights):
        c = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if c[i] != heights[i]: ans += 1
        return ans


sln = Solution()
example = [1, 1, 4, 2, 1, 3]
print(sln.heightChecker(example))