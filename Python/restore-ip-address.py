class Solution:
    def restoreIpAddresses(self, s):
        def solve(_s, idx, addr, ans):
            if idx == 4:
                if not _s:
                    ans.append(addr[:-1])
                return
            if len(_s) >= 1:
                solve(_s[1:], idx + 1, addr + _s[:1] + '.', ans)
            if len(_s) >= 2 and _s[0] != '0':
                solve(_s[2:], idx + 1, addr + _s[:2] + '.', ans)
            if len(_s) >= 3 and _s[0] != '0' and int(_s[:3]) <= 255:
                solve(_s[3:], idx + 1, addr + _s[:3] + '.', ans)

            return ans

        return solve(s, 0, "", [])
