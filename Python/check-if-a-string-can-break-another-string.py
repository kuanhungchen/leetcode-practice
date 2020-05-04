import heapq


class Solution:
    def checkIfCanBreak(self, s1, s2):
        stk1, stk2 = [], []
        for c1, c2 in zip(s1, s2):
            heapq.heappush(stk1, c1)
            heapq.heappush(stk2, c2)
        flag = 0
        while stk1:
            c1 = heapq.heappop(stk1)
            c2 = heapq.heappop(stk2)
            if c1 > c2:
                if flag == 0:
                    flag = 1
                elif flag == 2:
                    return False
            elif c2 > c1:
                if flag == 0:
                    flag = 2
                elif flag == 1:
                    return False
        return True
