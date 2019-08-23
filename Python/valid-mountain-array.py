class Solution:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        _up = True
        for idx in range(len(A)-1):
            if _up:
                if A[idx] < A[idx+1]:
                    continue
                elif A[idx] > A[idx+1] and idx != 0:
                    _up = not _up
                else:
                    return False
            else:
                if A[idx] > A[idx+1]:
                    continue
                else:
                    return False
        return not _up


class Solution2:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        turn_idx = -1
        for idx in range(len(A)-1):
            if A[idx] < A[idx+1]:
                continue
            elif A[idx] > A[idx+1] and idx != 0:
                turn_idx = idx
                break
            else:
                return False
        if turn_idx == -1:
            return False
        return len(A[turn_idx:]) == len(list(set(A[turn_idx:]))) and A[turn_idx:] == sorted(A[turn_idx:], reverse=True)
