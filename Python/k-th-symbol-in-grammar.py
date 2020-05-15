class Solution:
    def kthGrammar(self, N, K):

        flag = False
        while K != 1:
            i = 0
            while 2 ** i < K:
                i += 1
            K -= 2 ** (i - 1)
            flag = not flag
        return 1 if flag else 0
