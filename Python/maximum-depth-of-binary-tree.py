# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        return 0 if not root else max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
