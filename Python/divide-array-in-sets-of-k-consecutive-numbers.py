class Solution:
    def isPossibleDivide(self, nums, k):
        if len(nums) % k: return False
        if len(nums) == k: return True

        nums.sort()
        nxt = 1
        for i in range(len(nums)):
            if nums[i] == -1: continue
            tmp = [nums[i]]
            for j in range(nxt, len(nums)):
                if nums[j] == -1 or nums[j] == tmp[-1]:
                    continue
                elif nums[j] == tmp[-1] + 1:
                    if len(tmp) == 1: nxt = j
                    tmp.append(nums[j])
                    nums[j] = -1
                    if len(tmp) == k: break
                else:
                    return False
            nums[i] = -1
        return True
