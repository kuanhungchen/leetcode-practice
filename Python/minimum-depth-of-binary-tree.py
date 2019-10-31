# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        # DFS
        def solve(node, level):
            if not node: return level - 1
            elif node.left and node.right: return min(solve(node.left, level+1), solve(node.right, level+1))
            else: return max(solve(node.left, level+1), solve(node.right, level+1))
        return solve(root, 1)
