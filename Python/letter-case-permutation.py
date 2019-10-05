class Solution:
    def letterCasePermutation(self, S):
        ans = [S]
        for i in range(len(S)):
            if S[i].isalpha():
                idx, rng = 0, len(ans)
                while idx < rng:
                    a = ans[idx]
                    if a[i].isupper():
                        ans.append(a[:i]+a[i].lower()+a[i+1:])
                    else:
                        ans.append(a[:i]+a[i].upper()+a[i+1:])
                    idx += 1
        return ans
