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

        
        if (p.val < q.val) {
            smaller = p.val;
            bigger = q.val;
        } else {
            smaller = q.val;
            bigger = p.val;
        }
        
        if (smaller > root.val && bigger > root.val) {
            return lowestCommonAncestor(root.right, p, q);
        }
        if (smaller < root.val && bigger < root.val) {
            return lowestCommonAncestor(root.left, p, q);
        }
        return root;
    }
}