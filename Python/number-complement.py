class Solution:
    def findComplement(self, num):
        s = ""
        for c in bin(num)[2:]:
            if c == '1':
                s += '0'
            else:
                s += '1'
        return int(s, 2)


class Solution2:
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
