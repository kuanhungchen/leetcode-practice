class Solution:
    def longestDiverseString(self, a, b, c):
        def valid(s, c):
            return len(s) < 2 or not (s[-1] == c and s[-2] == c)

        s = ""
        x, y, z = [a, 'a'], [b, 'b'], [c, 'c']
        while x[0] or y[0] or z[0]:
            x, y, z = sorted([x, y, z], reverse=True)
            if x[0] and valid(s, x[1]):
                s += x[1]
                x[0] -= 1
            elif y[0] and valid(s, y[1]):
                s += y[1]
                y[0] -= 1
            elif z[0] and valid(s, z[1]):
                s += z[1]
                z[0] -= 1
            else:
                return s
        return s
