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
        //iterative approach
//         ListNode ans;
//         ListNode newListPointer;
        
//         if (list1 == null) {
//             return list2;
//         }
//         if (list2 == null) {
//             return list1;
//         }
//         if (list1.val <= list2.val) {
//             ans = new ListNode(list1.val);
//             list1 = list1.next;
//         } else {
//             ans = new ListNode(list2.val);
//             list2 = list2.next;
//         }
        
//         newListPointer = ans;
        
//         while (list1 != null || list2 != null) {
//             if (list1 == null) {
//                 newListPointer.next = list2;
//                 break;
//             }
//             if (list2 == null) {
//                 newListPointer.next = list1;
//                 break;
//             }
//             if (list1.val <= list2.val) {
//                 newListPointer.next = new ListNode(list1.val);
//                 list1 = list1.next;
//             } else {
//                 newListPointer.next = new ListNode(list2.val);
//                 list2 = list2.next;
//             }
//             newListPointer = newListPointer.next;
//         }
//         return ans;
        
        //recursive approach
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        if (list1.val <= list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
}