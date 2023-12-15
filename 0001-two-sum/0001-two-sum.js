/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = {};
    const ans = [];
    
    nums.forEach((num, index) => {
        if ((target - num) in seen) {
            ans.push(index, seen[target-num])
        } else {
            seen[num] = index;
        }
    });
    
    return ans;
};