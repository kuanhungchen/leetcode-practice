class Solution:
    def numTimesAllBlue(self, ls):
        tc = oc = bc = 0
        status = [0 for _ in range(len(ls) + 1)]
        status[0] = 2
        ans = 0

        for l in ls:
            tc += 1
            if status[l - 1] == 2:
                status[l] = 2
                bc += 1
                l += 1
                while l < len(status):
                    if status[l] == 0:
                        break
                    if status[l] == 1:
                        status[l] = 2
                        oc -= 1
                        bc += 1
                    l += 1
            else:
                status[l] = 1
                oc += 1

            if tc == bc: ans += 1
        return ans
