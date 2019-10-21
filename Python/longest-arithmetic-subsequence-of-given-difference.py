class Solution:
    def longestSubsequence(self, arr, difference):
        if difference == 0:
            from collections import Counter
            c = Counter(arr)
            ans = c.most_common(1)
            return ans[0][1]

        candidates = {arr[0]: 1}
        for i in range(1, len(arr)):
            if arr[i] - difference in candidates:
                tmp = candidates[arr[i]-difference]
                candidates.pop(arr[i]-difference)
                candidates[arr[i]] = tmp + 1
            elif arr[i] not in candidates:
                candidates[arr[i]] = 1
        _max = 0
        for k, v in candidates.items():
            _max = max(_max, v)
        return _max
