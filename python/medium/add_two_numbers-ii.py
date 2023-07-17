# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0
        l1_, l2_ = l1, l2

        while l1_:
            n1 = n1 * 10 + l1_.val
            l1_ = l1_.next

        while l2_:
            n2 = n2 * 10 + l2_.val
            l2_ = l2_.next

        n = n1 + n2

        l3 = ListNode()
        prev = None
        while n:
            l3.val = n % 10
            n //= 10
            next = ListNode()
            l3.next = prev
            prev = l3
            l3 = next

        if prev:
            return prev
        else:
            return ListNode(val=n)
