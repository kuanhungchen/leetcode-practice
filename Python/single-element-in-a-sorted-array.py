class Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if mid % 2:
                if nums[mid - 1] == nums[mid]:
                    left = mid
                elif nums[mid - 2] == nums[mid - 1]:
                    right = mid
                else:
                    return nums[mid - 1]
            else:
                if nums[mid] == nums[mid + 1]:
                    left = mid
                elif nums[mid + 1] == nums[mid + 2]:
                    right = mid
                else:
                    return nums[mid]
        return nums[right]
