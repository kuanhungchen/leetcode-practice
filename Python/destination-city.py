class Solution:
    def destCity(self, paths):
        dst = set()
        for path in paths:
            dst.add(path[1])

        for path in paths:
            if path[0] in dst:
                dst.remove(path[0])

        return list(dst)[0]
