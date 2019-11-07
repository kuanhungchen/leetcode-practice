class Solution:
    def groupAnagrams(self, strs):
        ans = {}
        for st in strs:
            cnt = [0 for _ in range(26)]
            for c in st:
                cnt[ord(c) - ord('a')] += 1
            if tuple(cnt) not in ans: ans[tuple(cnt)] = [st]
            else: ans[tuple(cnt)].append(st)
        return ans.values()
