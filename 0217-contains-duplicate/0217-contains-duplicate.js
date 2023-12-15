/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const seen = {};
    
    for (const num of nums) {
        if (seen[num]) {
            return true;
        }
        
        seen[num] = 1;
    }
    
    return false;
};