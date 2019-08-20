class Solution:
    def flipAndInvertImage(self, A):
        A = [A[i][::-1] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = 1 if A[i][j] == 0 else 0
        return A
