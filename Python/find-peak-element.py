class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = (left+right) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid
        return left if nums[left] > nums[right] else right


class Solution2:
    # RecursionError
    def findPeakElement(self, nums):
        return self.recursive(nums, 0, len(nums)-1)

    def recursive(self, nums, l, r):
        if l+1 == r:
            return l if nums[l] > nums[r] else r
        m = (l+r)//2
        if nums[m-1] < nums[m] > nums[m+1]:
            return m
        elif nums[m-1] > nums[m] > nums[m+1]:
            return self.recursive(nums, l, m)
        else:
            return self.recursive(nums, m, r)
