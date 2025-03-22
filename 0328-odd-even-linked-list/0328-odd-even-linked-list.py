# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # build the odd list and even list separately then combine at the end

        if not head or head.next == None:
            return head

        odd_curr = head
        even_head = even_curr = head.next

        while odd_curr and even_curr:
            odds_next = even_curr.next
            evens_next = None

            if odds_next:
                evens_next = odds_next.next

            odd_curr.next = odds_next
            even_curr.next = evens_next

            if not odds_next and not evens_next:
                odd_curr.next = even_head

            odd_curr = odd_curr.next
            even_curr = even_curr.next

            if odds_next and not evens_next:
                odd_curr.next = even_head

        return head


        


        