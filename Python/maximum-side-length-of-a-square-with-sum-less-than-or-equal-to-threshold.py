class Solution:
    def maxSideLength(self, A, thres):

        def getA(i, j):
            return A[i][j] if i >= 0 <= j else 0

        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] += getA(i - 1, j) + getA(i, j - 1) - getA(i - 1, j - 1)
                if A[i][j] <= thres and i >= ans <= j: ans += 1
        return ans
