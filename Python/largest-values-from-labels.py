class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):

        zipped = list(zip(values, labels))
        _dict = {x: 0 for x in set(labels)}
        ans = 0
        for v, l in reversed(sorted(zipped)):
            if num_wanted == 0:
                return ans
            if _dict[l] + 1 <= use_limit:
                ans += v
                num_wanted -= 1
                _dict[l] += 1
        return ans
