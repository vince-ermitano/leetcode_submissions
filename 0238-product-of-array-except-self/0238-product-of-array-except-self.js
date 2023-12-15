/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const leftProducts = [];
    const rightProducts = [];
    const ans = [];
    
    for (const num of nums) {
        if (leftProducts.length === 0) {
            leftProducts.push(num);
        } else {
            leftProducts.push(leftProducts[leftProducts.length - 1] * num)
        }
    }
    
    for (let i = nums.length-1; i >= 0; i--) {
        if (rightProducts.length === 0) {
            rightProducts.push(nums[i]);
        } else {
            rightProducts.unshift(rightProducts[0] * nums[i]);
        }
    }
    
    for (let i = 0; i < nums.length; i++) {
        if (i === 0) {
            ans.push(rightProducts[1]);
        } else if (i === nums.length-1) {
            ans.push(leftProducts[leftProducts.length-2])
        } else {
            ans.push(leftProducts[i-1] * rightProducts[i+1]);
        }
    }
    
    return ans;
};