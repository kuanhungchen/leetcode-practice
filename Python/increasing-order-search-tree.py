# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root):
        new_head = TreeNode(-1)
        self.rearrange(new_head, root)
        return new_head.right

    def rearrange(self, n_head, node):
        if node.left:
            n_head = self.rearrange(n_head, node.left)
        n_head.right = TreeNode(node.val)
        if node.right:
            n_head = self.rearrange(n_head.right, node.right)
            return n_head
        return n_head.right
