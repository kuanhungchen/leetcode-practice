# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def traversal(leaves, node):
            if not node:
                return leaves
            if not node.left and not node.right:
                leaves.append(node.val)
                return leaves
            leaves = traversal(leaves, node.left)
            leaves = traversal(leaves, node.right)
            return leaves
        return traversal([], root1) == traversal([], root2)


class Solution2:
    def leafSimilar(self, root1, root2):
        def traversal(leaves, node):
            return leaves if not node else leaves+[node.val] if not node.left and not node.right else traversal(traversal(leaves, node.left), node.right)
        return traversal([], root1) == traversal([], root2)
