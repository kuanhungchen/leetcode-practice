class Solution:
    def stoneGameIII(self, values):
        n = len(values)
        memo = {}

        def dfs(turn):
            if turn == n:
                return 0
            elif turn in memo:
                return memo[turn]
            take = 0
            memo[turn] = -1000
            for i in range(turn, min(n, turn + 3)):
                take += values[i]
                memo[turn] = max(memo[turn], take - dfs(i + 1))
            return memo[turn]

        score = dfs(0)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"
