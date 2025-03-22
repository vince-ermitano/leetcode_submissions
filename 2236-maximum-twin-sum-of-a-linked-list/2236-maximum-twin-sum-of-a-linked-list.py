# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse first half of the list while finding the midpoint of the list
        # one we hit the midpoint, iterate through the second half and the reversed first half
        # and find largest sum

        largest = 0
        prev = None
        curr = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next

            # reverse nodes
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        while curr:
            largest = max(largest, curr.val + prev.val)
            curr = curr.next
            prev = prev.next
        
        return largest




        