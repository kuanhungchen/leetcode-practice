class Solution:
    def simplifiedFractions(self, n):
        res = set()
        ans = []
        for i in range(2, n + 1):
            for j in range(1, i):
                num = float(j / i)
                if num not in res:
                    res.add(num)
                    ans.append(str(j) + "/" + str(i))
        return ans
