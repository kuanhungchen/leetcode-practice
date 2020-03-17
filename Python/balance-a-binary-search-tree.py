class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def balanceBST(self, root):

        def traversal(node):
            if not node: return
            traversal(node.left)
            sorted_array.append(node.val)
            traversal(node.right)

        def build(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            tmp = TreeNode(sorted_array[mid])
            tmp.left = build(start, mid - 1)
            tmp.right = build(mid + 1, end)
            return tmp

        sorted_array = []
        traversal(root)

        return build(0, len(sorted_array) - 1)
