# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, i = 1, 0
        node = head
        while node.next:
            n += 1
            node = node.next
        while i < n//2:
            i += 1
            head = head.next
        return head