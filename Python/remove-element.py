class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0

        tail = len(nums) - 1
        head = 0
        while head < tail:
            while nums[tail] == val and tail != 0:
                tail -= 1
            if head == tail:
                break
            while nums[head] != val and head != len(nums)-1:
                head += 1
            if head >= tail:
                break
            nums[head] = nums[tail]
            nums[tail] = val

        return len(nums) - nums.count(val)


class Solution2:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
