# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # my solution
        result = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            temp += carry

            result.next = ListNode((temp)%10)
            carry = temp//10
            result = result.next

        return head.next
