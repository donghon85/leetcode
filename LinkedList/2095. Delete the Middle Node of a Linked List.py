# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = i = 0
        cur = head

        # get length
        while cur:
            n += 1
            cur = cur.next

        if n == 1:  # except case
            return None

        # access the before middle node
        cur = head
        while i < n // 2 - 1:
            cur = cur.next
            i += 1

        # delete the middle node
        cur.next = cur.next.next

        return head