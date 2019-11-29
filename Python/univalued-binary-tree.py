# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root):
        def traversal(node, val):
            if not node: return True
            if node.val != val: return False
            return traversal(node.left, val) and traversal(node.right, val)
        return traversal(root, root.val)
