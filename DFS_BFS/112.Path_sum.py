# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = [False]
        if not root:
            return ans[0]

        def dfs(node, val):
            val += node.val

            if not node.left and not node.right:  # if leaf
                if val == targetSum:
                    ans[0] = True
                    return

            if node.left:
                dfs(node.left, val)
            if node.right:
                dfs(node.right, val)

            return

        dfs(root, 0)

        return ans[0]
