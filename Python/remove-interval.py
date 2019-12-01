class Solution:
    def removeInterval(self, intervals, remove):
        ans = []
        for interval in intervals:
            if interval[1] <= remove[0] or interval[0] >= remove[1]: ans.append(interval)
            elif remove[0] <= interval[0] and remove[1] >= interval[1]: pass
            elif remove[0] > interval[0] and remove[1] >= interval[1]: ans.append([interval[0], remove[0]])
            elif remove[0] <= interval[0] and remove[1] < interval[1]: ans.append([remove[1], interval[1]])
            else:
                ans.append([interval[0], remove[0]])
                ans.append([remove[1], interval[1]])
        return ans
