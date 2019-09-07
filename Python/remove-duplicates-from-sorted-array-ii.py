class Solution:
    def removeDuplicates(self, nums):
        # two pointer
        slow = fast = 0
        while fast < len(nums):
            while fast < len(nums) and nums[slow] == nums[fast]:
                fast += 1
            slow = fast
            if fast - slow > 2:
                for _ in range(fast - slow - 2):
                    nums.pop(slow)
                slow = fast = fast - (fast - slow - 2)
        return len(nums)


class Solution2:
    def removeDuplicates(self, nums):
        _pointer = 0
        while _pointer < len(nums):
            cur = nums[_pointer]
            _count = 0
            while _pointer < len(nums) and nums[_pointer] == cur:
                _pointer += 1
                _count += 1
            if _count > 2:
                nums[:] = nums[:_pointer-_count+2] + nums[_pointer:]
                _pointer = _pointer-_count+2
        return len(nums)
