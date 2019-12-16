class Solution:
    def canPlaceFlowers(self, pos, n):
        pos = [0] + pos + [0]
        for i in range(1, len(pos)-1):
            if n == 0: return True
            if not (pos[i] or pos[i-1] or pos[i+1]):
                pos[i] = 1
                n -= 1
        return n == 0
