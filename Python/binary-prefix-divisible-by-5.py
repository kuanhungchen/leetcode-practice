class Solution:
    def prefixesDivBy5(self, A):
        now = A[0]
        ans = [not now]
        for item in A[1:]:
            now = now * 2 + item
            ans.append(True if now % 5 == 0 else False)
        return ans


class Solution2:
    def prefixesDivBy5(self, A):
        # only need to record the modulo
        # faster because reduction of calculation on modulo
        now = A[0]
        ans = [not now]
        for item in A[1:]:
            now = ((now * 2 % 5) + item) % 5
            ans.append(now == 0)
        return ans
