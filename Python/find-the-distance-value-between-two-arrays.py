class Solution:
    def findTheDistanceValue(self, A, B, d):
        ans = 0
        for numA in A:
            flag = True
            for numB in B:
                dis = abs(numA - numB)
                if dis <= d:
                    flag = False
                    break
            ans += flag
        return ans
