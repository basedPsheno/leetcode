# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        len = 0
        cur_el = head
        while cur_el != None:
            len += 1
            cur_el = cur_el.next
        if len == 0:
            return True
        shift = len % 2
        middle = head
        for i in range(0, len//2 + shift):
            middle = middle.next
        prev_el = None
        cur_el = head
        for i in range(0, len//2):
            next_el = cur_el.next
            cur_el.next = prev_el
            prev_el = cur_el
            cur_el = next_el
        left = prev_el
        right = middle
        for i in range(0, len//2):
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
