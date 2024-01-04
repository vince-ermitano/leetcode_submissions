/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    let slow = head;
    let fast = head.next;
    
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    let rightHalf = slow.next;

    // reverse right half
    slow.next = null;
    prev = slow.next;
    
    while (rightHalf) {
        let next = rightHalf.next;
        rightHalf.next = prev;
        prev = rightHalf;
        rightHalf = next;
    }
    
    rightHalf = prev;
    let leftHalf = head;
    
    while (rightHalf) {
        let leftNext = leftHalf.next;
        let rightNext = rightHalf.next;
        
        leftHalf.next = rightHalf;
        rightHalf.next = leftNext;
        
        leftHalf = leftNext;
        rightHalf = rightNext;
    }
};