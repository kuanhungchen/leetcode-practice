class Solution:
    def removeDuplicates(self, s):
        slow = fast = 0
        while fast < len(s):
            cnt = -2
            while fast < len(s) and cnt and s[fast] == s[slow]:
                fast += 1
                cnt += 1
            if fast - slow > 1:
                s = s[:slow] + s[fast:]
                fast = slow = max(0, slow - 1)
            else:
                slow = fast
        return s
