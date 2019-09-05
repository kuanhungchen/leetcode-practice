class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1


class Solution2:
    def search(self, nums, target):
        return nums.index(target) if target in nums else -1


class Solution3:
    def search(self, nums, target):
        return ([-1] + [i for i in range(len(nums)) if nums[i] == target])[-1]
