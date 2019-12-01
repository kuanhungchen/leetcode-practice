class Solution:
    def pancakeSort(self, A):
        ans = []
        for target in range(len(A), 0, -1):
            where = A.index(target)
            if target == where + 1:
                continue
            if where != 0:
                A = A[:where+1][::-1] + A[where+1:]
                ans.append(where + 1)
            A = A[:target][::-1] + A[target:]
            ans.append(target)
        return ans
