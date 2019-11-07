class Solution:
    def minimumSwap(self, s1, s2):
        tmp = {'x': 0, 'y': 0}
        for c1, c2 in zip(s1, s2):
            if c1 != c2: tmp[c1] += 1
        return -1 if (tmp['x'] + tmp['y']) % 2 else tmp['x'] // 2 + tmp['y'] // 2 + 2 * (tmp['x'] % 2)
