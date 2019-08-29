class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        differences = []
        for idx in range(len(A)):
            if A[idx] != B[idx]:
                differences.append(idx)
                if len(differences) > 2:
                    return False

        if len(differences) == 1:
            return False
        elif len(differences) == 0:
            _dict = {}
            for char in A:
                if char not in _dict.keys():
                    _dict[char] = 1
                else:
                    return True
        else:
            return A[differences[0]] == B[differences[1]] and A[differences[1]] == B[differences[0]]
