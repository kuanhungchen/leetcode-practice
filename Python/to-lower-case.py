class Solution:
    def toLowerCase(self, s):
        return "".join([chr(ord(c)+32) if 65 <= ord(c) <= 90 else c for c in s])
