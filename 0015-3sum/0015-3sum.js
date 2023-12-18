/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a, b) => a - b);

    const ans = [];
    
    for (let outer = 0; outer < nums.length; outer++) {
        if (outer > 0 && nums[outer] === nums[outer-1]) {
            continue;
        }

        let left = outer + 1;
        let right = nums.length-1;

        // run two sum
        while (left < right && left < nums.length-1) {

            if (left > outer + 1 && nums[left] === nums[left-1]) {
                left += 1;
                continue;
            }


            if (nums[outer] + nums[left] + nums[right] < 0) {
                left += 1;
            } else if (nums[outer] + nums[left] + nums[right] > 0) {
                right -= 1;
            } else {
                ans.push([nums[outer], nums[left], nums[right]]);
                left += 1;
            }
        }   
    }

    return ans;
};