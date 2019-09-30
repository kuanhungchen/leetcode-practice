class Solution:
    def checkSubarraySum(self, nums, k):
        # copy from others
        # dynamic programming

        # every time calculate current sum % k
        # if the value appears before two numbers of current
        # it means that the two numbers must be multiple of k
        # for example: [23, 2, 4, 6, 7], k = 6
        # at 23, _occurred[5] = 0 is saved
        # at 2, _occurred[1] = 1 is saved
        # at 4, _occurred[5] exists (appears at 23) and is two numbers before 4
        # so that the sum of numbers between 23 to 4 (contains 4) must be a multiple of 6
        re = 0
        _occurred = {0: -1}
        for i, num in enumerate(nums):
            re = (re + num) % k if k else re + num
            if re not in _occurred:
                _occurred[re] = i
            if i - _occurred[re] > 1:
                return True
        return False
