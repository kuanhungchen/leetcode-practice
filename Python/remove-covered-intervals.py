class Solution:
    def removeCoveredIntervals(self, itvls):
        ss = []
        for itvl in itvls:
            flag = True
            i = 0
            while i < len(ss):
                s = ss[i]
                if itvl[0] <= s[0] and s[1] <= itvl[1]:
                    ss.remove(s)
                    i -= 1
                elif s[0] <= itvl[0] and itvl[1] <= s[1]:
                    flag = False
                    break
                i += 1
            if flag: ss.append(itvl)
        return len(ss)
