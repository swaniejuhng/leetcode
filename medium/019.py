# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # count = 0; hit_tail = False
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # my solution - failed when len(linked_list) == 1 and n == 1
        """
        curr = head
        if not curr:
            self.hit_tail = True; return
        self.removeNthFromEnd(curr.next, n)
        if self.hit_tail:
            self.count += 1
        # if n == 1 and self.count == 1:
        elif self.count == n + 1:
            curr.next = curr.next.next
        return head
        """

        # better solution
        fast = head; slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        # then advance both fast and slow now that they are n-th positions apart
        # when fast hits tail, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head
