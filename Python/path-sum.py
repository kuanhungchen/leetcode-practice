# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        if root:
            return self.recursive(root, sum)
        return False

    def recursive(self, node, _sum):
        if node.val == _sum and node.left is None and node.right is None:
            return True
        else:
            if node.left and node.right:
                return self.recursive(node.left, _sum-node.val) or self.recursive(node.right, _sum-node.val)
            elif node.left:
                return self.recursive(node.left, _sum-node.val)
            if node.right:
                return self.recursive(node.right, _sum-node.val)


class Solution2:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        elif root.val == sum and root.left is None and root.right is None:
            return True
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)