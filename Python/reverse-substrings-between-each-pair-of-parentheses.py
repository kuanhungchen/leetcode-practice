class Solution:
    def reverseParentheses(self, s):
        ans = []
        stacks = []
        for c in s:
            if c == '(':
                stacks.append([])
            elif c == ')':
                if len(stacks) == 1:
                    ans.extend(reversed(stacks[-1]))
                else:
                    stacks[-2].extend(reversed(stacks[-1]))
                stacks.pop(-1)
            else:
                if len(stacks):
                    stacks[-1].append(c)
                else:
                    ans.append(c)
        return "".join(ans)
