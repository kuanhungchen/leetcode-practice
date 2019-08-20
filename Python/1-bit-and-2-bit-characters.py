class Solution:
    def isOneBitCharacter(self, bits):
        if len(bits) == 1:
            return True
        idx = 0
        while True:
            if idx == len(bits) - 3 or idx == len(bits) - 2:
                break
            if bits[idx] == 1:
                idx += 2
            else:
                idx += 1

        if idx == len(bits) - 3:
            if bits[idx] == 1:
                return True
            if bits[idx + 1] == 0:
                return True
            return False
        if idx == len(bits) - 2:
            if bits[idx] == 1:
                return False
            return True


class Solution2:
    def isOneBitCharacter(self, bits):
        idx = 0
        ans = False
        while idx < len(bits):
            if bits[idx] == 1:
                idx += 2
                ans = False
            else:
                idx += 1
                ans = True
        return ans
