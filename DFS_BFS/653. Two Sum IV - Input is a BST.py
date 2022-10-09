# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        store = []

        def travel(node):
            if not node:
                return
            travel(node.left)
            store.append(node.val)
            travel(node.right)

        travel(root)

        left, right = 0, len(store) - 1

        while left < right:
            val = store[left] + store[right]
            if val == k:
                return True
            elif val < k:
                left += 1
            else:  # val > k
                right -= 1
        return False