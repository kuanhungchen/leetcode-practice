class Solution:
    def findAndReplacePattern(self, words, ptn):

        def solve(w):
            p = {}
            for i in range(len(w)):
                if ord(w[i]) not in p:
                    p[ord(w[i])] = [i]
                else:
                    p[ord(w[i])].append(i)
            return sorted(p.values())

        std = solve(ptn)
        ans = []
        for word in words:
            if solve(word) == std: ans.append(word)
        return ans
