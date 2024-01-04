/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let curr1 = list1;
    let curr2 = list2;
    
    let dummy = new ListNode();
    let merged = dummy;
    
    while (curr1 && curr2) {
        if (curr1.val <= curr2.val) {
            merged.next = curr1;
            curr1 = curr1.next;
        } else {
            merged.next = curr2;
            curr2 = curr2.next;
        }
        
        merged = merged.next;
    }
    
    if (curr1) {
        merged.next = curr1;
    }
    
    if (curr2) {
        merged.next = curr2;
    }
    
    return dummy.next;
};