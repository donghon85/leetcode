# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaf1 = []
        self.leaf2 = []

        def check_leaf(node, leaf):
            if node is None:    return
            if not node.left and not node.right:
                leaf.append(node.val)

            check_leaf(node.left, leaf)
            check_leaf(node.right, leaf)

        check_leaf(root1, self.leaf1)
        check_leaf(root2, self.leaf2)

        return True if self.leaf1 == self.leaf2 else False

