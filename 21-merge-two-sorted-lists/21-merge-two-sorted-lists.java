/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode ans;
        ListNode newListPointer;
        
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        if (list1.val <= list2.val) {
            ans = new ListNode(list1.val);
            list1 = list1.next;
        } else {
            ans = new ListNode(list2.val);
            list2 = list2.next;
        }
        
        newListPointer = ans;
        
        int count = 0;
        
        while (list1 != null || list2 != null) {
            count++;
            if (list1 == null) {
                newListPointer.next = list2;
                break;
            }
            if (list2 == null) {
                newListPointer.next = list1;
                break;
            }
            if (list1.val <= list2.val) {
                newListPointer.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                newListPointer.next = new ListNode(list2.val);
                list2 = list2.next;
            }
            newListPointer = newListPointer.next;
        }
        System.out.println(count);
        return ans;
    }
}