class Solution:
    def divisorGame(self, N):
        # dynamic programming method
        # so hard, copy from others

        DP = [False for _ in range(N+1)]
        # suppose i is A's turn, then A can win if P[i] is True,
        # so that the result is P[N]. (Because Alice starts from N)

        for i in range(2, N+1):  # bottom-up, fill the DP from i = 2
            for j in range(1, i):  # range of move: 1 < j < i
                if i % j == 0 and not DP[i-j]:
                    # If we can find j such that i % j = 0 and DP[i-j] is False,
                    # it means that the person in (i-j) turn will lose,
                    # so that the person in i turn will win (b/c he can choose j as his move)
                    # that is why we fill DP[i] with True
                    DP[i] = True

        return DP[N]


class Solution2:
    def divisorGame(self, N):
        # After filling DP, we can know that only even terms is True
        # so that a faster method comes out.
        # but I think it's kind of cheating b/c it's hard to directly know this fact.
        return N % 2 == 0
