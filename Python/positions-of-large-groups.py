class Solution:
    def largeGroupPositions(self, S):
        S = S + '$'
        ans = []
        start = 0
        now = S[start]
        for index in range(1, len(S)):
            if S[index] != now:
                if index - start >= 3:
                    ans.append([start, index-1])
                start = index
                now = S[index]

        return ans
