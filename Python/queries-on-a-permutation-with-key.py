class Solution:
    def processQueries(self, queries, m):
        ans = []
        for i, q in enumerate(queries):
            ans.append(q - 1)
            tmp = {}
            flag = False
            for qq in queries[:i]:
                if qq == q:
                    ans[-1] = 0
                    flag = True
                    tmp = {}
                elif qq > q and qq not in tmp:
                    tmp[qq] = 1
                    ans[-1] += 1
                elif flag and qq != q and qq not in tmp:
                    tmp[qq] = 1
                    ans[-1] += 1
        return ans
