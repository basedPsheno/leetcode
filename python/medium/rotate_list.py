# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if k == 0:
            return head

        n = 1
        node = head

        while node.next != None:
            n += 1
            node = node.next

        k %= n
        if k == 0:
            return head
        node = head

        for i in range(n - k - 1):
            node = node.next

        new_head = node.next
        node.next = None
        new_node = new_head

        while new_node.next != None:
            new_node = new_node.next

        new_node.next = head


        return new_head
        
