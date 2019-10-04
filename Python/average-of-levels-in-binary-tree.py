# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root):

        def solve(cal1):
            re = []
            num = sm = 0
            while len(cal1):
                now = cal1.pop()
                num += 1
                sm += now.val
                if now.left:
                    re.append(now.left)
                if now.right:
                    re.append(now.right)
            return sm / num, re

        ans = []
        _do = [root]
        while len(_do):
            avg, _do = solve(_do)
            ans.append(avg)
        return ans
