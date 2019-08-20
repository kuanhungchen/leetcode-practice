class Solution:
    def getRow(self, rowIndex):
        last = [1]
        for _ in range(rowIndex):
            tmp = [1]
            for idx in range(len(last)-1):
                tmp.append(last[idx]+last[idx+1])

            tmp.append(1)
            last = tmp

        return last


example = 17
sln = Solution()
print(sln.getRow(example))
