/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let res = Number.POSITIVE_INFINITY;
    
    let left = 0;
    let right = nums.length-1;
    
    while (left <= right) {
        
        if (nums[left] <= nums[right]) {
            res = Math.min(nums[left], res);
            break;
        }
        const mid = Math.floor((left + right) / 2);
        
        res = Math.min(res, nums[mid]);
        
        // left sorted portion
        if (nums[mid] >= nums[left]) {
            left = mid + 1;
        } else { //right sorted portion
            right = mid-1;
        }
    }
    
    return res;
};