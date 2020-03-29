class Solution:
    def numTeams(self, rating):
        pos = {}
        for i, num in enumerate(rating):
            pos[num] = i

        ans = 0
        rating = sorted(rating)
        for i, x in enumerate(rating):
            for j, y in enumerate(rating[i + 1:]):
                for z in rating[i + j + 1:]:
                    if pos[x] > pos[y] > pos[z] or pos[x] < pos[y] < pos[z]:
                        ans += 1
        return ans
