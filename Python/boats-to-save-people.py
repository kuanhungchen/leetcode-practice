class Solution:
    def numRescueBoats(self, weights, limit):
        weights.sort()
        ans = len(weights)
        left, right = 0, len(weights) - 1
        while left < right:
            if weights[left] + weights[right] <= limit:
                ans -= 1
                left += 1
                right -= 1
            else:
                right -= 1
        return ans
