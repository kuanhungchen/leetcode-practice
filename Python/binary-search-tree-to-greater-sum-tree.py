class Solution:
    def bstToGst(self, root):
        def traversal(node, sm):
            if not node:
                return sm
            sm = traversal(node.right, sm)
            node.val = sm = sm + node.val
            sm = traversal(node.left, sm)
            return sm

        traversal(root, 0)
        return root
