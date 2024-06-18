/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let dp = Array(nums.length).fill(Infinity);
    dp[nums.length-1] = 0;
    
    for (let i = nums.length - 2; i >= 0; i--) {
        
        for (let j = 1; j <= nums[i]; j++) {
            dp[i] = Math.min(dp[i], 1 + dp[Math.min(nums.length-1, i + j)])
        }
    }
    
    console.log(dp);
    
    return dp[0];
};