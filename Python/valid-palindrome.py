class Solution:
    def isPalindrome(self, s):
        sentence = ""
        for char in s:
            if char.isalnum():
                sentence += char
        a, b = sentence[:len(sentence)//2], sentence[(len(sentence)+1)//2:]
        for pair in zip(a, b[::-1]):
            if pair[0].lower() != pair[1].lower():
                return False
        return True


class Solution2:
    def isPalindrome(self, s):
        slow, fast = 0, len(s)-1
        while slow < fast:
            while slow < len(s) and not s[slow].isalnum():
                slow += 1
            while fast >= 0 and not s[fast].isalnum():
                fast -= 1
            if slow >= fast:
                return True
            if s[slow].lower() != s[fast].lower():
                return False
            slow += 1
            fast -= 1
        return True


class Solution3:
    def isPalindrome(self, s):
        # copy from others
        s = ''.join(x.lower() for x in s if x.isalnum())
        return s == s[::-1]
