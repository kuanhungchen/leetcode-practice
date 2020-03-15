class Solution:
    def luckyNumbers(self, mat):

        def solve(i, m):
            for row in mat:
                if row[i] > m: return False
            return True

        ans = []
        for row in mat:
            idx, mn = [], 10 ** 6
            for i, ele in enumerate(row):
                if ele < mn:
                    idx = [i]
                    mn = ele
                elif ele == mn:
                    idx.append(i)

            for i in idx:
                if solve(i, mn): ans.append(mn)
        return ans
