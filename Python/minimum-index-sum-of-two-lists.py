class Solution:
    def findRestaurant(self, list1, list2):
        mp1, mp2 = {x: i for i, x in enumerate(list1)}, {x: i for i, x in enumerate(list2)}
        ans = [10 ** 4, []]
        for k, v in mp1.items():
            if k in mp2 and v + mp2[k] == ans[0]: ans[1].append(k)
            elif k in mp2 and v + mp2[k] < ans[0]: ans = [v + mp2[k], [k]]
        return ans[1]
