class Solution:
    # tmp is used to prevent same value of slow
    def twoSum(self, numbers, target):
        tmp = numbers[0] + 1
        for slow in range(len(numbers)):
            if numbers[slow] == tmp:
                continue
            tmp = slow
            for fast in range(slow+1, len(numbers)):
                if numbers[slow] + numbers[fast] == target:
                    return [slow+1, fast+1]
                elif numbers[slow] + numbers[fast] > target:
                    break


class Solution2:
    # faster because using binary search on value of fast
    def twoSum(self, numbers, target):
        tmp = numbers[0] + 1
        for slow in range(len(numbers)):
            if numbers[slow] == tmp:
                continue
            tmp = slow
            left = slow
            right = len(numbers)
            fast = (right + left) // 2
            while True:
                if numbers[slow] + numbers[fast] == target:
                    return [slow+1, fast+1]
                elif numbers[slow] + numbers[fast] > target:
                    f = (fast + left) // 2
                    right = fast
                else:
                    f = (fast + right) // 2
                    left = fast
                if f == fast:
                    break
                fast = f
