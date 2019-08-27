class Solution:
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
