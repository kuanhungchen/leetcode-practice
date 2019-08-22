class Solution:
    def plusOne(self, digits):
        for idx in range(len(digits)-1, -1, -1):
            if 1 + digits[idx] == 10:
                digits[idx] = 0
            else:
                digits[idx] += 1
                break

        if digits[0] == 0:
            ans = [1]
            ans.extend(digits)
            return ans
        else:
            return digits
