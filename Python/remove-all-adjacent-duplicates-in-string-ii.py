class Solution:
    def removeDuplicates(self, s, k):
        cnt = 1
        i = 1
        while i < len(s):
            if s[i] == s[i-1]:
                cnt += 1
                if cnt == k:
                    s = s[:i-k+1] + s[i+1:]
                    cnt = 1
                    i = 1
                else:
                    i += 1
            else:
                cnt = 1
                i += 1
        return s


class Solution2:
    def removeDuplicates(self, s, k):
        # using stack
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)
