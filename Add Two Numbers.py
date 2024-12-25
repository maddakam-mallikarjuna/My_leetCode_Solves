# My solution for this Problem....

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(max(m, n))      # Space Complexity: O(max(m, n))

        dummy = ListNode()
        res = dummy

        carry = 0

        while l1 or l2 or carry:  # Continue until both lists and carry are processed
            add = carry

            if l1:
                add += l1.val
                l1 = l1.next
            
            if l2:
                add += l2.val
                l2 = l2.next

            temp = add % 10
            carry = add // 10

            dummy.next = ListNode(temp)
            dummy = dummy.next

        return res.next
