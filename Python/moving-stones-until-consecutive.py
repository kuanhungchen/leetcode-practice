class Solution:
    def numMovesStones(self, a, b, c):
        return [0 if max(a, b, c) - min(a, b, c) == 2 else 2 if abs(b-a) > 2 and abs(c-b) > 2 and abs(a-c) > 2 else 1, max(a, b, c) - min(a, b, c) + 1 - 3]
