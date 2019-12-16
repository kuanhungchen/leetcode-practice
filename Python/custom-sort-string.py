class Solution:
    def customSortString(self, S, T):
        pr_s = {c: i for i, c in enumerate(S)}
        cnt_t = {}
        for c in T:
            if c not in cnt_t: cnt_t[c] = 1
            else: cnt_t[c] += 1
        ans = [""] * 27
        for k, v in cnt_t.items():
            if k in pr_s: ans[pr_s[k]] = k * v
            else: ans[-1] += k * v
        return ''.join(ans)
