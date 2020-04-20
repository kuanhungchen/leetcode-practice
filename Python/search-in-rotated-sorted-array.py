class Solution:
    def search(self, nums, target):
        def bs(start, end, target):
            left = start
            right = end
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] == target: return mid
                if nums[mid] > target > nums[0]:
                    right = mid
                elif target > nums[mid] > nums[0]:
                    left = mid
                elif target > nums[0] > nums[mid]:
                    right = mid
                elif nums[mid] < target < nums[0]:
                    left = mid
                elif target < nums[mid] < nums[0]:
                    right = mid
                elif target < nums[0] < nums[mid]:
                    left = mid

            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            return -1

        if not nums: return -1
        if nums[0] == target: return 0
        return bs(0, len(nums) - 1, target)
