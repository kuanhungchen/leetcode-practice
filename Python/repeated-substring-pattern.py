class Solution:
    def repeatedSubstringPattern(self, s):
        for i in range(1, len(s)):
            if len(s) % i != 0:
                continue
            pattern = s[:i]

            flag = True
            for j in range(i, len(s), len(pattern)):
                if pattern == s[j:j+len(pattern)]:
                    continue
                flag = False
                break
            if flag is True:
                return True
        return False
