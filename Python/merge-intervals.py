class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        _len = len(intervals)
        idx = 0
        while idx < _len - 1:
            if intervals[idx][1] >= intervals[idx+1][0]:
                intervals[idx][1] = max(intervals[idx][1], intervals[idx+1][1])
                intervals.pop(idx+1)
                _len -= 1
            else:
                idx += 1
        return intervals
