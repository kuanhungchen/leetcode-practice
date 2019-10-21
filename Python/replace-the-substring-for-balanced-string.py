class Solution:
    def balancedString(self, s):
        def solve(d, require):
            for k, v in require.items():
                if d[k] < v:
                    return False
            return True

        _dict = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for c in s:
            _dict[c] += 1
        quota = len(s) // 4
        require = {k: v - quota if v > quota else 0 for k, v in _dict.items()}

        _min = len(s)
        slow, fast = 0, 0
        _now = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        while fast < len(s):
            while fast < len(s) and not solve(_now, require):
                _now[s[fast]] += 1
                fast += 1
            _min = min(_min, fast - slow)

            while slow < len(s) and solve(_now, require):
                _min = min(_min, fast - slow)
                _now[s[slow]] -= 1
                slow += 1

            if fast >= len(s):
                return _min

        return _min
