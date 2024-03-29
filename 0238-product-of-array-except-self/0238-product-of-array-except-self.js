/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const ans = Array(nums.length).fill(1);
    
    let prefix = 1;
    
    for (let i = 0; i < nums.length; i++) {
        ans[i] = prefix;
        prefix *= nums[i];
    }
    
    let postfix = 1;
    
    for (let i = nums.length-1; i >= 0; i--) {
        ans[i] *= postfix;
        postfix *= nums[i];
    }
    
    return ans;
};