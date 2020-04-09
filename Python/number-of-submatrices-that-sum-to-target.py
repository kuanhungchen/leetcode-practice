class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y + 1] += matrix[x][y]

        ans = 0
        for y1 in range(n):
            for y2 in range(y1, n):
                preSum = {0: 1}
                s = 0
                for x in range(m):
                    s += matrix[x][y2] - (matrix[x][y1 - 1] if y1 > 0 else 0)
                    ans += preSum.get(s - target, 0)
                    preSum[s] = preSum.get(s, 0) + 1
        return ans
