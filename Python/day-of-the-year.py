class Solution:
    def dayOfYear(self, date):
        # copy from others
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = map(int, date.split('-'))
        ans = 0
        ans += sum(months[:m-1]) + d
        if m > 2:
            if y % 400 == 0: ans += 1
            if y % 100 == 0: return ans
            if y % 4 == 0: ans += 1
        return ans
