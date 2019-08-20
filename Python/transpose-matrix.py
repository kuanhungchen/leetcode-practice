class Solution:
    def transpose(self, A):
        ans = [[]] * len(A[0])
        for i in range(len(A[0])):
            tmp = A[:]
            for j in range(len(A)):
                tmp[j] = tmp[j][i]
            ans[i] = tmp
        return ans


class Solution2:
    def transpose(self, A):
        ans = [[0] * len(A) for _ in range(len(A[0]))]
        for r in range(len(A)):
            tmp = A[r]
            for c in range(len(tmp)):
                ans[c][r] = tmp[c]

                print(ans)
        return ans
