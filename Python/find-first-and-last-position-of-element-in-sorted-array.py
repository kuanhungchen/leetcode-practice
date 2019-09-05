class Solution:
    def searchRange(self, nums, target):
        # suppose nums = [1, 5, 5, 8, 8, 10], target = 8
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        ans = []

        # use binary search to find the leftmost
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                # Because we need to find the left-MOST,
                # though nums[3] equals to 8 already,
                # we still need to continue the iteration,
                # otherwise there maybe a more left 8.
                right = mid

        # left = 2, right = 3
        # nums[left] = 5, nums[right] = 8
        # Now we need to determine which is the leftmost.
        # (sometimes nums[left] may equal to target, then leftmost is nums[left])
        if nums[left] == target:
            ans.append(left)
        elif nums[right] == target:
            ans.append(right)
        else:
            return [-1, -1]

        # If the leftmost is the tail, return [left, left]
        if ans[0] == len(nums) - 1:
            ans.extend(ans)
            return ans

        # use binary search to find the rightmost
        left, right = ans[0], len(nums)-1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                # because we are finding the edge,
                # we use '>' instead of '=='
                right = mid
            else:
                left = mid + 1

        # determine which is the rightmost
        if nums[left] > target:
            ans.extend([left-1])
        elif nums[right] > target:
            ans.extend([right-1])
        else:
            # if both are not larger than target,
            # then they must both equal to target while the next number is larger than target
            ans.extend([min(right+1, len(nums)-1) - 1])
        return ans
