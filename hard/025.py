# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # my solution - failed to solve
        """
        curr = head
        stop = False

        while curr:
            ptr = curr
            for i in range(k):
                print(curr.next.val)
                if curr.next is None:
                    stop = True
                    break
                curr = curr.next

            if stop:
                break

            print()
            curr = ptr
            for i in range(k-1):
                ptr = curr.next
                print(ptr.val)
                curr.next = curr.next.next
                curr.next.next = curr

            curr = curr.next
        return head
        """

        # better solution


five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

a = Solution()
a.reverseKGroup(one, 3)
