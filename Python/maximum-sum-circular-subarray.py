class Solution:
    def maxSubarraySumCircular(self, nums):
        cur_mx, sum_mx, cur_mn, sum_mn, total = 0, -float('inf'), 0, float('inf'), 0
        for num in nums:
            cur_mx = max(num, cur_mx + num)
            sum_mx = max(sum_mx, cur_mx)
            cur_mn = min(num, cur_mn + num)
            sum_mn = min(sum_mn, cur_mn)
            total += num

        return sum_mx if sum_mx <= 0 else max(sum_mx, total - sum_mn)
