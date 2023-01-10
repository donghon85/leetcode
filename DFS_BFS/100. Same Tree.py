# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ansl, ansr = [], []

        def dfs(node, ans):
            if not node:
                ans.append('null')
                return
            ans.append(node.val)
            dfs(node.left, ans)
            dfs(node.right, ans)

        dfs(p, ansl)
        dfs(q, ansr)

        return ansl == ansr