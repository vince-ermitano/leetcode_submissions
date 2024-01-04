/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
    let curr = head;
    let nodeMap = new Map();
    nodeMap.set(null, null);
    
    while (curr) {
        nodeMap.set(curr, new Node(curr.val));
        curr = curr.next;
    }
    
    curr = head;
    
    while (curr) {
        nodeMap.get(curr).next = nodeMap.get(curr.next);
        nodeMap.get(curr).random = nodeMap.get(curr.random);
        curr = curr.next;
    }
    
    return nodeMap.get(head);
    
    
};