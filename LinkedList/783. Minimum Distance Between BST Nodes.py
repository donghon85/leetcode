# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node):
            if not node: return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        ans.sort(reverse=True)
        return min([ans[i] - ans[i+1] for i in range(len(ans)-1)])