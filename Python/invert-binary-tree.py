class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        def bfs(last, node, s):
            if node.left:
                s[last + 'l'] = node.left.val
                bfs(last + 'l', node.left, s)
            if node.right:
                s[last + 'r'] = node.right.val
                bfs(last + 'r', node.right, s)

        def construct(last, node, s):
            if last + 'r' in s:
                node.left = TreeNode(s[last + 'r'])
                construct(last + 'r', node.left, s)
            if last + 'l' in s:
                node.right = TreeNode(s[last + 'l'])
                construct(last + 'l', node.right, s)
            return node

        if not root:
            return root
        elif not root.left and not root.right:
            return root

        s = {}
        bfs('', root, s)
        bfs('', root, s)
        return construct('', TreeNode(root.val), s)
