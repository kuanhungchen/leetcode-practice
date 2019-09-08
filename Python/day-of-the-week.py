class Solution:
    def dayOfTheWeek(self, day, month, year):
        import datetime
        return datetime.date(year, month, day).strftime('%A')
