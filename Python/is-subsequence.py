class Solution:
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        idx = 0
        target = s[idx]
        for c in t:
            if c == target:
                if idx == len(s)-1:
                    return True
                idx += 1
                target = s[idx]
        return False
