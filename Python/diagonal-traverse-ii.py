class Solution:
    def findDiagonalOrder(self, nums):
        pos = []
        for i, row in enumerate(nums):
            for y in range(len(row)):
                pos.append([i, y])
        pos = sorted(pos, key=lambda x: [x[0] + x[1], -x[0]])
        ans = []
        for p in pos:
            ans.append(nums[p[0]][p[1]])
        return ans
