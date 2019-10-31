# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self.lowestCommonAncestor(root.left, p, q) if p.val < root.val > q.val else self.lowestCommonAncestor(root.right, p, q) if p.val > root.val < q.val else root
