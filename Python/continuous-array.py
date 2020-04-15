class Solution:
    def findMaxLength(self, nums):
        mp = {0: -1}
        cnt = ans = 0
        for i, num in enumerate(nums):
            cnt += 1 if num else -1
            if cnt not in mp: mp[cnt] = i
            else: ans = max(i - mp[cnt], ans)
        return ans
