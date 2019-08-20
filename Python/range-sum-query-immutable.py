class NumArray:
    # copy from others
    # self.array[i] = sum(nums[:i])
    # sumRange(m, n) = array[n] - array[m]
    def __init__(self, nums):
        if len(nums) == 0:
            self.array = [0]
        elif len(nums) == 1:
            self.array = [nums[0]]

        if len(nums) > 1:
            for i in range(1, len(nums)):
                self.array.append(self.array[-1] + nums[i])
        '''
        more simple:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        self.array = nums
        '''

    def sumRange(self, i, j):
        return self.array[j] - self.array[i-1] if i != 0 else self.array[j]
