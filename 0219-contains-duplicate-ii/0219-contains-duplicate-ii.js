/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const seen = {};
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in seen) {
            if (i - seen[nums[i]]<= k) return true;
            
            seen[nums[i]] = i;
        } else {
            seen[nums[i]] = i;
        }
    }
    
    return false;
};