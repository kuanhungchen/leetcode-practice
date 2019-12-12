class Solution:
    def firstUniqChar(self, s):
        if not s: return -1
        occur = {}
        for i in range(len(s)):
            if s[i] not in occur: occur[s[i]] = i
            elif occur[s[i]] != -1: occur[s[i]] = 10 ** 7
        return min(occur.values()) if min(occur.values()) != 10 ** 7 else -1
