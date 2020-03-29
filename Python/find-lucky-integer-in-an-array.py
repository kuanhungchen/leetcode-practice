class Solution:
    def findLucky(self, arr):
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        mx = -1
        for k, v in d.items():
            if k == v:
                mx = max(mx, k)
        return mx
