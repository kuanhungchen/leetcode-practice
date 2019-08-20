class Solution:
    def isToeplitzMatrix(self, matrix):
        tmp = matrix[0]
        for row in matrix[1:]:
            for i in range(len(matrix[0])-1):
                if tmp[i] != row[i+1]:
                    return False
            tmp = row
        return True


sln = Solution()
example = [
  [1, 2, 3],
  [5, 1, 2],
  [9, 5, 2]
]
print(sln.isToeplitzMatrix(example))
