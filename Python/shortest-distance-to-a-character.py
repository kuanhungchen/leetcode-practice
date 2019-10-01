class Solution:
    def shortestToChar(self, S, C):
        zero_positions = {}
        for x in range(len(S)):
            if S[x] == C: zero_positions[x] = 1
        zes = list(zero_positions.keys())
        zes.append(10**6)
        ans = []
        for i in range(len(S)):
            if i in zero_positions.keys():
                ans.append(0)
            else:
                tmp = 10**6
                for j in range(len(zes)):
                    if abs(i - zes[j]) >= tmp:
                        ans.append(tmp)
                        break
                    else:
                        tmp = abs(i - zes[j])
        return ans
