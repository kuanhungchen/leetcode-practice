class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        _len = len(needle)
        for idx in range(len(haystack)-_len+1):
            if haystack[idx:idx+_len] == needle:
                return idx
        return -1
