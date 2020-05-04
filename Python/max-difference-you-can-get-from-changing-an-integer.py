class Solution:
    def maxDiff(self, num):
        s = str(num)
        ss = str(num)
        if s[0] != '1':
            tar = s[0]
            for i in range(len(s)):
                if s[i] == tar:
                    s = s[:i] + '1' + s[i + 1:]
            a = int(s)
        else:
            tar = None
            for i in range(1, len(s)):
                if not tar and s[i] != '0' and s[i] != s[0]:
                    tar = s[i]
                    s = s[:i] + '0' + s[i + 1:]
                elif s[i] == tar:
                    s = s[:i] + '0' + s[i + 1:]
            a = int(s)

        if ss[0] != '9':
            tar = ss[0]
            for i in range(len(ss)):
                if ss[i] == tar:
                    ss = ss[:i] + '9' + ss[i + 1:]
            b = int(ss)
        else:
            tar = None
            for i in range(len(ss)):
                if not tar and ss[i] != '9':
                    tar = ss[i]
                    ss = ss[:i] + '9' + ss[i + 1:]
                elif ss[i] == tar:
                    ss = ss[:i] + '9' + ss[i + 1:]
            b = int(ss)
        return b - a
