class Solution:
    def moveZeroes(self, nums):
        non_zero = 0
        zero = 0
        leng = len(nums)
        while True:
            while zero < leng and nums[zero] != 0:
                zero += 1
            if zero == leng: break

            non_zero = zero + 1
            while non_zero < leng and nums[non_zero] == 0:
                non_zero += 1
            if non_zero == leng: break

            nums[zero] = nums[non_zero]
            nums[non_zero] = 0


class Solution2:
    def moveZeroes(self, nums):
        # much faster
        zero, non_zero = 0, 0
        leng = len(nums)
        while zero < leng and nums[zero] != 0:
            zero += 1
        if zero == leng: return

        non_zero = zero + 1
        while non_zero < leng:
            if nums[non_zero] != 0:
                nums[zero] = nums[non_zero]
                nums[non_zero] = 0
                zero += 1
            non_zero += 1
