class Solution:
    def subarraySum(self, nums, k):
        mp = {0: 1}
        sm = ans = 0
        for num in nums:
            sm += num
            if sm - k in mp:
                ans += mp[sm - k]
            if sm not in mp: mp[sm] = 1
            else: mp[sm] += 1
        return ans
