/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    const dp = Array.from({ length: obstacleGrid.length }, () => Array(obstacleGrid[0].length).fill(0));
    
    dp[0][0] = obstacleGrid[0][0] !== 1;
    
    const rows = obstacleGrid.length;
    const columns = obstacleGrid[0].length;
    
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            if (i === 0 && j === 0) {
                continue;
            }
            
            let isObstacle = obstacleGrid[i][j] === 1;
            
            if (!isObstacle) {
                if (i-1 >= 0 && j-1 >= 0) {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                } else if (i-1 >= 0) {
                    dp[i][j] = dp[i-1][j];
                } else {
                    dp[i][j] = dp[i][j-1];
                }
            } else {
                dp[i][j] = 0;
            }
        }
    }
    
    return dp[rows-1][columns-1];
};