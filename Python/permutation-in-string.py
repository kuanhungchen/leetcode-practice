import collections


class Solution:
    def checkInclusion(self, s1, s2):
        mp1 = collections.defaultdict(int)
        for c in s1:
            mp1[c] += 1

        window = 0
        for i, c in enumerate(s2):
            while mp1[c] == 0 and window:
                mp1[s2[i - window]] += 1
                window -= 1
            if mp1[c] > 0:
                mp1[c] -= 1
                window += 1
            if window == len(s1):
                return True
        return False
