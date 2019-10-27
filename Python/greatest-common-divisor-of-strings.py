class Solution:
    # 8/27/2019
    def gcdOfStrings(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        ans = [""]
        if len1 > len2:
            for idx in range(len2, 0, -1):
                divisor = str2[:idx]
                f = True
                if len1 % len(divisor) != 0 or len2 % len(divisor) != 0:
                    continue
                for j in range(len1 // len(divisor)):
                    if str1[j*len(divisor):(j+1)*len(divisor)] != divisor:
                        f = False
                        break
                    if j == len1 // len(divisor) - 1:
                        f = False
                        ans.append(divisor)
                if f:
                    for j in range(len2 // len(divisor)):
                        if str2[j*len(divisor):(j+1)*len(divisor)] != divisor:
                            break
                        if j == len2 // len(divisor) - 1:
                            ans.append(divisor)
        else:
            for idx in range(len1, 0, -1):
                divisor = str1[:idx]
                f = True
                if len1 % len(divisor) != 0 or len2 % len(divisor) != 0:
                    continue
                for j in range(len2 // len(divisor)):
                    if str2[j*len(divisor):(j+1)*len(divisor)] != divisor:
                        f = False
                        break
                    if j == len2 // len(divisor) - 1:
                        f = False
                        ans.append(divisor)
                if f:
                    for j in range(len1 // len(divisor)):
                        if str1[j*len(divisor):(j+1)*len(divisor)] != divisor:
                            break
                        if j == len1 // len(divisor) - 1:
                            ans.append(divisor)
        return max(ans)


class Solution2:
    # 10/25/2019
    def gcdOfStrings(self, s, t):

        def solve(_s, _t, _d):
            return _s == _d * (len(_s) // len(_d)) and _t == _d * (len(_t) // len(_d))

        if len(s) < len(t):
            s, t = t, s

        i = 1
        d = t
        while len(d):
            if len(s) % len(d) or len(t) % len(d):
                i += 1
                d = t[:len(t) // i]
            else:
                if solve(s, t, d):
                    return d
                else:
                    i += 1
                    d = t[:len(t) // i]
        return d
