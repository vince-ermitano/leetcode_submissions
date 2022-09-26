/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int smaller;
        int bigger;
        
        if (root == null) {
            return null;
        }
        
        if (p.val < q.val) {
            smaller = p.val;
            bigger = q.val;
        } else {
            smaller = q.val;
            bigger = p.val;
        }
        
        if (root.val == smaller || root.val == bigger) {
            return root;
        } 
        
        if (root.val > smaller && root.val < bigger) {
            return root;
        }
        
        TreeNode leftResult = lowestCommonAncestor(root.left, p, q);
        TreeNode rightResult = lowestCommonAncestor(root.right, p, q);
        
        return leftResult == null ? rightResult : leftResult;
    }
}