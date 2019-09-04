class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # two-pass algorithm
        # first pass for counting colors
        # second pass for re-filling
        # T: O(n), S: O(1)
        colors = [0, 0, 0]
        for num in nums:
            colors[num] += 1
        for idx in range(len(nums)):
            if colors[0] != 0:
                nums[idx] = 0
                colors[0] -= 1
            elif colors[1] != 0:
                nums[idx] = 1
                colors[1] -= 1
            else:
                nums[idx] = 2
                colors[2] -= 1


class Solution2:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        _cur, _two = 0, len(nums)
        for _ in range(len(nums)):
            if nums[_cur] == 2:
                nums.pop(_cur)
                nums.append(2)
                _two -= 1
            elif nums[_cur] == 1:
                nums.pop(_cur)
                nums.insert(_two-1, 1)
            else:
                _cur += 1


example = [2, 0, 2]
sln = Solution2()
sln.sortColors(example)
print(example)
"""

2, 0, 2, 1, 2, 1, z=0, t=N
0, 2, 1, 2, 1, 2, z=0, t=5
0, 2, 1, 2, 1, 2, z=1, t=5
0, 1, 2, 1, 2, 2, z=1, t=4
0, 2, 1, 1, 2, 2, z=1, t=4
0, 1, 1, 2, 2, 2, z=1, t=3 
0, 1, 1, 2, 2, 2, z=1, t=3
"""