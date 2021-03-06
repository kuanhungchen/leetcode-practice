class Solution:
    def matrixScore(self, A):
        def toggle(row, matrix, idx):
            # function to toggle a row or column
            if row:
                for i in range(len(matrix[0])):
                    matrix[idx][i] = 1 if matrix[idx][i] == 0 else 0
                return matrix
            else:
                ret = []
                for row in matrix:
                    row[idx] = 1 if row[idx] == 0 else 0
                    ret.append(row)
                return ret

        for i in range(len(A)):
            # check each row, toggle if first item is zero
            if A[i][0] == 0:
                toggle(True, A, i)
        for i in range(len(A[0])):
            # check each column, toggle if number of zero > number of one
            cnt_1, cnt_0 = 0, 0
            for row in A:
                if row[i]:
                    cnt_1 += 1
                else:
                    cnt_0 += 1
            if cnt_1 < cnt_0:
                toggle(False, A, i)
        sm = 0
        for row in A:
            # sum up the answer
            num = "".join([str(row[i]) for i in range(len(row))])
            sm += int(num, 2)
        return sm
