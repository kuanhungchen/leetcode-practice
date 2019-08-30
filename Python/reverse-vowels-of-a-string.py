class Solution:
    def reverseVowels(self, s):
        left = 0
        right = len(s) - 1
        while True:
            while left < len(s) and not self._vowel(s[left]):
                left += 1
            if left >= right:
                return s
            while right >= 0 and not self._vowel(s[right]):
                right -= 1
            if left == right:
                return s
            s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]
            left += 1
            right -= 1

    @staticmethod
    def _vowel(c):
        c = c.lower()
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'


class Solution2:
    def reverseVowels(self, s):
        # faster
        left = 0
        right = len(s) - 1
        s = list(s)
        while True:
            while left < len(s) and not self._vowel(s[left]):
                left += 1
            if left >= right:
                return "".join(s)
            while right >= 0 and not self._vowel(s[right]):
                right -= 1
            if left == right:
                return "".join(s)
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    @staticmethod
    def _vowel(c):
        c = c.lower()
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'
