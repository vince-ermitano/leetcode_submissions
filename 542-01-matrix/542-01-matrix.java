class Solution {
    
    public int[][] updateMatrix(int[][] mat) {
        int ans[][] = new int[mat.length][mat[0].length];
        
        for (int i = 0; i < ans.length; i++) {
            for (int j = 0; j < ans[0].length; j++) {
                ans[i][j] = Integer.MAX_VALUE - 10000;
            }
        }
        
        //top-to-bottom (checking left and top of cell)
        for (int i = 0; i < ans.length; i++) {
            for (int j = 0; j < ans[0].length; j++) {
                if (mat[i][j] == 0) {
                    ans[i][j] = 0;
                } else {
                    if (i > 0) {
                        ans[i][j] = Math.min(ans[i][j], ans[i-1][j] + 1);
                    }
                    if (j > 0) {
                        ans[i][j] = Math.min(ans[i][j], ans[i][j-1] + 1);
                    }
                }
            }
        }
        
        //bottom-to-top (checking bottom and right of cell)
        for (int i = ans.length - 1; i >= 0; i--) {
            for (int j = ans[0].length - 1; j >= 0; j--) {
                if (ans[i][j] == 0) {
                    continue;
                }
                if (i < ans.length - 1) {
                    ans[i][j] = Math.min(ans[i+1][j] + 1, ans[i][j]);
                }
                if (j < ans[0].length - 1) {
                    ans[i][j] = Math.min(ans[i][j+1] + 1, ans[i][j]);
                }
            }
        }
        
        return ans;
    }
}