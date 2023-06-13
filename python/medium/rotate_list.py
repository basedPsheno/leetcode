# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        n = 1
        node = head

        while node.next:
            n += 1
            node = node.next

        k %= n
        node.next = head
        temp_node = head

        for _ in range(n - k - 1):
            temp_node = temp_node.next

        new_head = temp_node.next
        temp_node.next = None


        return new_head
        
