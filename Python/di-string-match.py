class Solution:
    def diStringMatch(self, S):
        record = {'I': 1, 'D': -1}
        ans = [0]
        for c in S:
            ans.append(record[c])
            record[c] += 1 if c == 'I' else -1
        return [x - record['D'] - 1 for x in ans]
