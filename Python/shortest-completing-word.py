class Solution:
    def shortestCompletingWord(self, std, words):
        stddic = {}
        for c in std.lower():
            if c.isalpha() and c not in stddic:
                stddic[c] = 1
            elif c.isalpha() and c in stddic:
                stddic[c] += 1

        ans = "xxxxxxxxxxxxxxxxxxx"
        for word in words:
            worddic = {}
            for c in word.lower():
                if c.isalpha() and c not in worddic:
                    worddic[c] = 1
                elif c.isalpha() and c in worddic:
                    worddic[c] += 1

            flag = True
            for k, v in stddic.items():
                if k not in worddic or (worddic[k] < v):
                    flag = False
                    break
            if flag and len(word) < len(ans): ans = word

        return ans
