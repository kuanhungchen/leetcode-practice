# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        nodes = [[root], []]
        x, h = 0, 0
        while root:
            h += 1
            cnt = 0
            while nodes[x]:
                node = nodes[x].pop(0)
                if not node.right:
                    return 2 ** h - 1 + cnt + (node.left is not None)
                else:
                    nodes[(x + 1) % 2].append(node.left)
                    nodes[(x + 1) % 2].append(node.right)
                    cnt += 2
            x = (x + 1) % 2

        return 0
