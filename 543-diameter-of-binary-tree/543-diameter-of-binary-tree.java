/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int ans;

    public int diameterOfBinaryTree(TreeNode root) {
        this.ans = 0;
        dfs(root);
        return this.ans;
    }
    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int longestRight = dfs(root.right);
        int longestLeft = dfs(root.left);

        ans = Math.max(ans, longestRight + longestLeft);

        return Math.max(longestLeft, longestRight) + 1;
    }
}