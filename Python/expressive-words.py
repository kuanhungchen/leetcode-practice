class Solution:
    def expressiveWords(self, s, words):
        def solve(_word):
            tmp = _word[0]
            tmp_idx = 0
            groups = []
            for i, c in enumerate(_word):
                if c != tmp:
                    groups.append([tmp, i - tmp_idx])
                    tmp = c
                    tmp_idx = i
            groups.append([tmp, len(_word) - tmp_idx])
            return groups

        def isStretchy(std_grps, grps):
            if len(grps) != len(std_grps):
                return False
            for std_grp, grp in zip(std_grps, grps):
                if grp[0] != std_grp[0] or std_grp[1] < 3 and grp[1] != std_grp[1] or grp[1] > std_grp[1]:
                    return False
            return True

        s_grps = solve(s)
        ans = 0
        for word in words:
            word_grps = solve(word)
            if isStretchy(s_grps, word_grps):
                ans += 1
        return ans
