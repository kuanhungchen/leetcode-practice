class Solution:
    def removeOuterParentheses(self, S):

        ans = ""
        stk = []
        cnt = 0
        for c in S:
            if cnt == 0:
                if stk: stk.pop()
                ans += "".join(stk)
                stk = []
                cnt += 1
            else:
                if c == '(':
                    cnt += 1
                    stk.append('(')
                else:
                    cnt -= 1
                    stk.append(')')
        stk.pop()
        ans += "".join(stk)
        return ans
