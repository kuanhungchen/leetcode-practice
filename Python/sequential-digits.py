class Solution:
    def sequentialDigits(self, low, high):
        ans = []
        for start in range(1, 9):
            num = start
            while num <= high:
                if low <= num: ans.append(num)
                if num % 10 == 9: break
                num = num * 10 + (num % 10) + 1
        return sorted(ans)
