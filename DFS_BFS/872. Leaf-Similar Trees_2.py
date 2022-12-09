# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, low, high):
            if not node: return

            self.ans = max(self.ans, abs(node.val-high), abs(node.val - low))

            if node.val < low:
                low = node.val
            if node.val > high:
                high = node.val
            dfs(node.left, low, high)
            dfs(node.right, low, high)
        dfs(root, root.val, root.val)
        return self.ans