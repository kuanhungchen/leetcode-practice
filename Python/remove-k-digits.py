class Solution:
    def removeKdigits(self, num, k):
        _stack = []
        for digit in num:
            while _stack and k > 0:
                if _stack[-1] > digit:
                    _stack.pop(-1)
                    k -= 1
                else:
                    break
            _stack.append(digit)

        if k: _stack[:] = _stack[:-k]
        while _stack and _stack[0] == '0': _stack.pop(0)

        return "".join(_stack) if _stack else "0"
