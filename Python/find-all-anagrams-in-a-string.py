import collections


class Solution:
    def findAnagrams(self, s, p):
        mp = collections.defaultdict(int)
        std = collections.defaultdict(int)

        for c in p:
            std[c] += 1
        ans = []
        cur, window = 0, len(p)
        for idx in range(len(s)):
            if cur < window - 1:
                mp[s[idx]] += 1
                cur += 1
            elif cur == window - 1:
                mp[s[idx]] += 1
                cur += 1
            else:
                mp[s[idx - window]] -= 1
                mp[s[idx]] += 1

            if cur == window:
                flag = True
                for k, v in std.items():
                    if mp[k] != v:
                        flag = False
                        break
                if flag:
                    ans.append(idx - window + 1)
        return ans
