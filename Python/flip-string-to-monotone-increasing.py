class Solution:
    def minFlipsMonoIncr(self, S):
        ones = [0]
        for num in S:
            ones.append(ones[-1] + int(num))
        return min(ones[i] + len(S) - i - (ones[-1] - ones[i]) for i in range(len(ones)))
