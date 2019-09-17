class Solution:
    def largestTimeFromDigits(self, A):
        times = [[A[0] * 10 + A[1], A[2] * 10 + A[3]],
                 [A[0] * 10 + A[1], A[3] * 10 + A[2]],
                 [A[1] * 10 + A[0], A[2] * 10 + A[3]],
                 [A[1] * 10 + A[0], A[3] * 10 + A[2]],
                 [A[0] * 10 + A[2], A[1] * 10 + A[3]],
                 [A[0] * 10 + A[2], A[3] * 10 + A[1]],
                 [A[2] * 10 + A[0], A[1] * 10 + A[3]],
                 [A[2] * 10 + A[0], A[3] * 10 + A[1]],
                 [A[0] * 10 + A[3], A[1] * 10 + A[2]],
                 [A[0] * 10 + A[3], A[2] * 10 + A[1]],
                 [A[3] * 10 + A[0], A[1] * 10 + A[2]],
                 [A[3] * 10 + A[0], A[2] * 10 + A[1]]]
        _largest = [-1, -1]
        for idx in range(len(times)):
            if 0 <= times[idx][0] <= 23 and 0 <= times[idx][1] <= 59:
                if times[idx][0] > _largest[0] or (times[idx][0] == _largest[0] and times[idx][1] > _largest[1]):
                    _largest = times[idx]
            if 0 <= times[idx][1] <= 23 and 0 <= times[idx][0] <= 59:
                if times[idx][1] > _largest[0] or (times[idx][1] == _largest[0] and times[idx][0] > _largest[1]):
                    _largest = [times[idx][1], times[idx][0]]
        return "" if _largest == [-1, -1] else str(_largest[0]).zfill(2) + ':' + str(_largest[1]).zfill(2)
