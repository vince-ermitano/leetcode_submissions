/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let res = Number.POSITIVE_INFINITY;
    
    let left = 0;
    let right = nums.length-1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        res = Math.min(res, nums[mid]);
        
        // left sorted portion
        if (nums[mid] >= nums[left]) {
            res = Math.min(res, nums[left]);
            left = mid + 1;
        } else {
            right = mid-1;
        }
    }
    
    return res;
};