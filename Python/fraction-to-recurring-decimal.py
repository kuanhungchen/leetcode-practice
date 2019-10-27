class Solution:
    def fractionToDecimal(self, n, d):
        ans = ""
        if n // d < 0:
            ans += '-'
            n, d = abs(n), abs(d)
        _dict = {}

        Q = n // d
        R = n % d
        ans += str(Q)
        if not R:
            return ans
        ans += '.'
        start = len(ans)
        while R != 0:
            n = 10 * R
            Q = n // d
            R = n % d
            if tuple([Q, R]) in _dict and Q != 0:
                return ans[:_dict[tuple([Q, R])]] + '(' + ans[_dict[tuple([Q, R])]:] + ')'
            elif tuple([Q, R]) in _dict and Q == 0:
                ans += str(Q)
            elif tuple([Q, R]) not in _dict:
                ans += str(Q)
                _dict[tuple([Q, R])] = start
                start += 1

        return ans
