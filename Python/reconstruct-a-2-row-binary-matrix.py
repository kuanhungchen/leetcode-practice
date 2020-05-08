class Solution:
    def reconstructMatrix(self, upper, lower, cols):
        n = len(cols)
        ans = [[0 for _ in range(n)] for _ in range(2)]

        u, l = upper, lower
        for i, col in enumerate(cols):
            if col == 2:
                ans[0][i] = ans[1][i] = 1
            elif col == 1:
                if upper >= lower:
                    ans[0][i] = 1
                    upper -= 1
                else:
                    ans[1][i] = 1
                    lower -= 1
        if sum(ans[0]) == u and sum(ans[1]) == l: return ans
        return []
