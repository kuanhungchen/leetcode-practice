# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, root):
        def traversal(node, s):
            if not node: return s
            s += str(node.val)
            if not (node.left or node.right): return s
            s = traversal(node.left, s + "(") + ")"
            if node.right: s = traversal(node.right, s + "(") + ")"
            return s

        return traversal(root, "")
