class Solution:
    def calPoints(self, ops):
        stk = []
        ans = 0
        for op in ops:
            if op == 'C' and stk:
                ans -= stk.pop()
            elif op == 'D' and stk:
                stk.append(2 * stk[-1])
                ans += stk[-1]
            elif op == '+' and len(stk) >= 2:
                stk.append(stk[-1] + stk[-2])
                ans += stk[-1]
            else:
                ans += int(op)
                stk.append(int(op))
        return ans
