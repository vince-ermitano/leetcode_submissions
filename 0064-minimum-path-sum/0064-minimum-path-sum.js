/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    let dp = Array.from({ length: grid.length }, () => Array(grid[0].length).fill(0))
    
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (i-1 < 0 && j-1 < 0) {
                dp[i][j] = grid[i][j];
            } else if (i-1 < 0) {
                dp[i][j] = dp[i][j-1] + grid[i][j];
            } else if (j-1 < 0) {
                dp[i][j] = dp[i-1][j] + grid[i][j];
            } else {
                dp[i][j] = Math.min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j]);
            }
        }
    } 
    
    return dp[grid.length-1][grid[0].length-1];
};