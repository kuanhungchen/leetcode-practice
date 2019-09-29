class Solution:
    def equalSubstring(self, s, t, maxCost):
        # sliding window
        _arr = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]

        i = 0
        for j in range(len(_arr)):
            maxCost -= _arr[j]
            if maxCost < 0:
                maxCost += _arr[i]
                i += 1
        return j - i + 1
