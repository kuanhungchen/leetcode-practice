class Solution:
    def numberOfSubstrings(self, s):
        psum = [[0, 0, 0]]
        for c in s:
            if c == 'a':
                tmp = psum[-1][:]
                tmp[0] += 1
                psum.append(tmp)
            elif c == 'b':
                tmp = psum[-1][:]
                tmp[1] += 1
                psum.append(tmp)
            else:
                tmp = psum[-1][:]
                tmp[2] += 1
                psum.append(tmp)

        ans = 0
        n = len(psum)
        for i in range(n - 1, -1, -1):
            if psum[i][0] == 0 or psum[i][1] == 0 or psum[i][2] == 0:
                return ans
            for j in range(i - 1, -1, -1):
                if psum[i][0] - psum[j][0] == 0 or psum[i][1] - psum[j][1] == 0 or psum[i][2] - psum[j][2] == 0:
                    continue
                ans += j + 1
                break
        return ans
