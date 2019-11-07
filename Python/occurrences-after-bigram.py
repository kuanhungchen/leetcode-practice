class Solution:
    def findOcurrences(self, text, first, second):
        words = text.split(' ')
        ans = []
        for i in range(2, len(words)):
            if words[i-2] == first and words[i-1] == second:
                ans.append(words[i])
        return ans
