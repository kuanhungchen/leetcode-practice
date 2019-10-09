# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def traversal(self, node):
        if not node:
            return
        self._dict[node.val] = 1
        self.traversal(node.right)
        self.traversal(node.left)

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:

        self._dict = {}
        self.traversal(root1)
        nodes = [root2]
        while len(nodes):
            node = nodes.pop(-1)
            if target - node.val in self._dict: return True
            if node.left: nodes.append(node.left)
            if node.right: nodes.append(node.right)
        return False
