/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let gas = 0;
    
    for (let num of nums) {
        if (gas < 0) {
            return false;
        } else {
            gas = Math.max(gas, num);
            gas -= 1;
        }
    }
    
    return true;
};