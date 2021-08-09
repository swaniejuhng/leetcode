# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # my solution - not working, why?
        """
        first = head; second = head.next
        prev = None
        head = second
        while first and second:
            first.next = second.next
            second.next = first
            if prev:
                prev.next = second
            prev = first
            first = second.next
            second = first.next
        return head
        """

        # better solution
        prev, prev.next = self, head
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            prev.next, b.next, a.next = b, a, b.next
            prev = a
        return self.next
