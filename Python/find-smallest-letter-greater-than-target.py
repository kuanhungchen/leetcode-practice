class Solution:
    def nextGreatestLetter(self, letters, target):
        return chr(min([ord(x) - ord(target) if ord(x) - ord(target) > 0 else ord(x) - ord(target) + 26 for x in letters]) + ord(target)) if chr(min([ord(x) - ord(target) if ord(x) - ord(target) > 0 else ord(x) - ord(target) + 26 for x in letters]) + ord(target)).isalpha() else chr(min([ord(x) - ord(target) if ord(x) - ord(target) > 0 else ord(x) - ord(target) + 26 for x in letters]) + ord(target)-26)
