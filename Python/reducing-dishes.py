class Solution:
    def maxSatisfaction(self, ss):
        pick = 0
        score = 0
        ss.sort()
        for i, s in enumerate(ss[::-1]):
            if score >= score + pick + s:
                break
            score += pick + s
            pick += s
        return score
