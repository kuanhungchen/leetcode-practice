class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root):
        def dfs(node):
            if not node:
                return 0
            if not node.children:
                return 1
            return 1 + max([dfs(child) for child in node.children])

        return dfs(root)
