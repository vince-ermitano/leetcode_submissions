# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find midpoint of list
        # build lists of first half of the values
        # and second half of the values
        # iterate through both lists to find max sum

        slow = head
        fast = head.next
        first_half = []
        second_half = []

        while fast.next:
            first_half.append(slow.val)

            slow = slow.next
            fast = fast.next.next

        first_half.append(slow.val)
        slow = slow.next
        
        
        while slow:
            second_half.append(slow.val)
            slow = slow.next
        
        print(first_half)
        print(second_half)

        max_twin_sum = float('-inf')
        for i in range(len(first_half)):
            max_twin_sum = max(max_twin_sum, first_half[i] + second_half[len(first_half) - 1 - i])
        
        return max_twin_sum

        # [5]
        # []


        