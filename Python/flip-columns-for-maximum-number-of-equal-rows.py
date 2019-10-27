class Solution:
    def maxEqualRowsAfterFlips(self, m):
        _dict = {}
        for row in m:
            if tuple(row) not in _dict:
                _dict[tuple(row)] = 1
            else:
                _dict[tuple(row)] += 1
            flipped_row = [1 if x == 0 else 0 for x in row]
            if tuple(flipped_row) not in _dict:
                _dict[tuple(flipped_row)] = 1
            else:
                _dict[tuple(flipped_row)] += 1
        return max(_dict.values())
