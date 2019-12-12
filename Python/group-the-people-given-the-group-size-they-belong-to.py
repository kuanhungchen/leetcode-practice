class Solution:
    def groupThePeople(self, groupSizes):
        from collections import defaultdict
        groups = defaultdict(list)
        for i, size in enumerate(groupSizes):
            if len(groups[size]) == 0 or len(groups[size][-1]) == size:
                groups[size].append([i])
            else:
                groups[size][-1].append(i)

        ans = []
        for v in groups.values():
            ans.extend(v)
        return ans
