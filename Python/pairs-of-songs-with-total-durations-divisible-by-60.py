class Solution:
    def numPairsDivisibleBy60(self, time):
        length = [0 for _ in range(60)]
        for t in time:
            length[t % 60] += 1

        ans = 0

        ans += length[0] * (length[0] - 1) // 2  # 0
        for idx in range(1, 30):  # 1 to 29
            ans += length[idx] * length[60-idx]
        ans += length[30] * (length[30] - 1) // 2  # 30

        return ans
