class Solution:
    def maxScoreWords(self, words, letters, scores):
        costs = [[0 if chr(ord('a') + i) not in word else word.count(chr(ord('a') + i)) for i in range(26)] for word in
                 words]
        total = [0 if chr(ord('a') + i) not in letters else letters.count(chr(ord('a') + i)) for i in range(26)]
        prizes = [sum([scores[ord(c) - ord('a')] for c in word]) for word in words]

        def solve(quota, score, idx):
            if idx == len(words): return score
            new_quota = []
            for q, c in zip(quota, costs[idx]):
                if q < c: return solve(quota, score, idx + 1)
                new_quota.append(q - c)
            return max(solve(new_quota, score + prizes[idx], idx + 1), solve(quota, score, idx + 1))

        return solve(total, 0, 0)
