class Solution:
    def validPalindrome(self, s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return s[:i]+s[i+1:] == (s[:i]+s[i+1:])[::-1] or s[:len(s)-i-1]+s[len(s)-i:] == (s[:len(s)-i-1]+s[len(s)-i:])[::-1]
        return True
