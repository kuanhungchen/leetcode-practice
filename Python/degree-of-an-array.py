class Solution:
    def findShortestSubArray(self, nums):
        if len(set(nums)) == len(nums):
            return 1
        freqs = {}
        for num in nums:
            if num not in freqs.keys():
                freqs[num] = nums.count(num)

        max_freq = max(freqs.values())
        min_length = len(nums) + 1
        checked = []
        for start in range(len(nums)):
            if freqs[nums[start]] != max_freq or nums[start] in checked:
                continue
            for end in range(len(nums)-1, start, -1):
                if nums[start] != nums[end]:
                    continue
                if min_length > end - start + 1:
                    min_length = end - start + 1
                break
            checked.append(nums[start])
        return min_length
