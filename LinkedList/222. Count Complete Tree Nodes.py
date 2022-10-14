# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def depthLeft(node):
            d = 0
            while node:
                node = node.left
                d += 1
            return d

        def depthRight(node):
            d = 0
            while node:
                node = node.right
                d += 1
            return d

        l, r = depthLeft(root.left), depthRight(root.right)

        if l == r:
            return 2 ** (l + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)