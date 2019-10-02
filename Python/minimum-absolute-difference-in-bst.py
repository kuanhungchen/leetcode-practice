# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root):
        def traversal(node):
            ans = []
            if node:
                ans.extend(traversal(node.left))
                ans.append(node.val)
                ans.extend(traversal(node.right))
            return ans

        nodes = sorted(traversal(root))
        return min([abs(nodes[i + 1] - nodes[i]) for i in range(len(nodes) - 1)])

