# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # my solution - time exceeded
        """
        result = head = ListNode(0)
        lists = [l for l in lists if l is not None]
        while lists:
            min_idx = 0
            for i in range(len(lists)):
                if lists[min_idx].val > lists[i].val:
                    min_idx = i
            result.next = lists[min_idx]
            result = result.next
            lists[min_idx] = lists[min_idx].next
            lists = [l for l in lists if l is not None]

        return head.next
        """

        # better solution
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        result = head = ListNode(0)
        while l and r:
            if l.val <= r.val:
                result.next = l
                l = l.next
            else:
                result.next = r
                r = r.next
            result = result.next
        result.next = l or r
        return head.next
