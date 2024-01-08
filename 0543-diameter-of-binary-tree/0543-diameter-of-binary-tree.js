/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
    let res = 0;
    
    function dfs(root) {
        if (!root) return -1;
        
        let leftHeight = dfs(root.left);
        let rightHeight = dfs(root.right);
        
        res = Math.max(2 + leftHeight + rightHeight, res);
        
        return Math.max(leftHeight, rightHeight) + 1; 
    }
    
    dfs(root);
    
    return res;
};