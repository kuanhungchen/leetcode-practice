class Solution:
    def longestSubarray(self, nums, k):
        maxq, minq = [], []
        slow = fast = 0
        ans = 0
        while fast < len(nums):
            while minq and nums[fast] <= nums[minq[-1]]:
                minq.pop()
            while maxq and nums[fast] >= nums[maxq[-1]]:
                maxq.pop()

            minq.append(fast)
            maxq.append(fast)

            while nums[maxq[0]] - nums[minq[0]] > k:
                slow += 1
                if maxq[0] < slow:
                    maxq.pop(0)
                if minq[0] < slow:
                    minq.pop(0)
            ans = max(ans, fast - slow + 1)
            fast += 1
        return ans
