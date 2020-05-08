class Solution:
    def oddCells(self, n, m, indices):
        rows, cols = {}, {}
        for r, c in indices:
            if r in rows:
                rows[r] += 1
            else:
                rows[r] = 1
            if c in cols:
                cols[c] += 1
            else:
                cols[c] = 1

        ans = 0
        for i in range(n):
            for j in range(m):
                sm = 0
                if i in rows:
                    sm += rows[i]
                if j in cols:
                    sm += cols[j]
                if sm % 2 == 1:
                    ans += 1
        return ans

