/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let left = 0;
    let right = nums.length-1;
    
    while (left <= right) {
        
        const m = Math.floor((left + right) / 2);
        
        if (nums[m] === target) {
            return m;
        }
        
        if (nums[left] <= nums[m]) {
            if (nums[left] <= target && target <= nums[m]) {
                right = m-1;
            } else {
                left = m+1;
            }
        } else {
            if (nums[m] <= target && target <= nums[right]) {
                left = m+1;
            } else {
                right = m-1;
            }
        }
        
    }
    return -1;
};