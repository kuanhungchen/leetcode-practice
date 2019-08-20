class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        ans = [[1]]

        for _ in range(1, numRows):
            tmp = [1]
            for idx in range(len(ans[-1])-1):
                tmp.append(ans[-1][idx] + ans[-1][idx+1])
            tmp.append(1)
            ans.append(tmp)

        return ans


example = 0
sln = Solution()
result = sln.generate(example)
print(result)
