class Solution:
    def maximumProduct(self, nums):
        # The maximum can be:
        # 1. multiplying three largest nums
        # 2. multiplying largest one and two negative nums largest in magnitude (smallest)

        # Sorting-based method, complexity > O(n)

        nums = sorted(nums)
        return max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1])


class Solution2:
    def maximumProduct(self, nums):
        # go through numbers and keep track of three largest and two smallest
        # numbers is enough to decide the maximum product

        # complexity should be O(n)

        _max = [-1000, -1000, -1000]  # from small to large
        _min = [1000, 1000]  # from large to small

        for num in nums:
            if num > _max[2]:
                _max = [_max[1], _max[2], num]
            elif num > _max[1]:
                _max = [_max[1], num, _max[2]]
            elif num > _max[0]:
                _max = [num, _max[1], _max[2]]

            if num < _min[1]:
                _min = [_min[1], num]
            elif num < _min[0]:
                _min = [num, _min[1]]

        return max(_max[0]*_max[1], _min[0]*_min[1])*_max[2]
