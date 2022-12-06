# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

### it has a O(1) space complexity
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        curOdd = head # last odd node / curOdd.next -> the first even odd
        node = head
        pre = node # the last even node
        count = 2
        node = node.next

        while node is not None:
            if count % 2 == 0:
                pre = node
                node = node.next
            else:
                new = node.next
                pre.next = node.next
                temp = curOdd.next
                curOdd.next = node
                curOdd = node
                curOdd.next = temp
                node = new
            count += 1
        return head