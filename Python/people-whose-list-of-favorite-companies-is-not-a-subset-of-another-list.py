class Solution:
    def peopleIndexes(self, Cs):
        oldCmaps = []
        for i, C in enumerate(Cs):
            oldCmaps.append([i, set(C)])

        Cmaps = sorted(oldCmaps, key=lambda x: len(list(x[1])), reverse=True)
        ans = [Cmaps[0][0]]
        for Cmap in Cmaps[1:]:
            print(ans, Cmap[0])
            flag2 = True
            for ansCi in ans:
                flag = False
                for curCom in list(Cmap[1]):
                    if curCom not in oldCmaps[ansCi][1]:
                        flag = True
                        break
                if not flag:
                    flag2 = False
                    break
            if flag2:
                ans.append(Cmap[0])

        return sorted(ans)
