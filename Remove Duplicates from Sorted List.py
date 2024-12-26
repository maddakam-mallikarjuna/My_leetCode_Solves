# My solution for this Problem....

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n)      # Space Complexity: O(1)

        res = head  # Keep a reference to the head of the list

        while head and head.next:  # Traverse the list
            if head.val == head.next.val:  # If current and next node values are the same
                head.next = head.next.next  # Skip the duplicate node
            else:
                head = head.next  # Move to the next node if no duplicate

        return res  # Return the head of the modified list
