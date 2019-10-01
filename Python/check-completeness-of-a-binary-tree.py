# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCompleteTree(self, root):
        nodes = [[root], []]
        for level in range(8):
            complete = True
            nodes[(level + 1) % 2] = []
            for node in nodes[level % 2]:
                if node.left:
                    if not complete:
                        return False
                    nodes[(level + 1) % 2].append(node.left)
                else:
                    complete = False
                if node.right:
                    if not complete:
                        return False
                    nodes[(level + 1) % 2].append(node.right)
                else:
                    complete = False
            if not complete:
                for node in nodes[(level + 1) % 2]:
                    if node.left or node.right:
                        return False
                return True
