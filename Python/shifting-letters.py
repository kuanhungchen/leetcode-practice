class Solution:
    def shiftingLetters(self, S, shifts):
        base = ord('a')
        ans = ""
        total_shift = sum(shifts[:])
        for idx in range(len(S)):
            ans += chr((ord(S[idx]) + total_shift - base) % 26 + base)
            total_shift = total_shift - shifts[idx]
        return ans
