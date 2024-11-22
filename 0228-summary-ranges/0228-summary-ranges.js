/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    ans = [];
    
    let start = 0;
    
    while (start < nums.length) {
        
        let beginning = nums[start];
        let end = nums[start];
        
        while (start + 1 < nums.length && nums[start] === nums[start+1] - 1) {
            end += 1;
            start += 1;
        }
        
        if (beginning === end) {
            ans.push(beginning.toString());
        } else {
            ans.push(beginning.toString() + "->" + end.toString());
        }
        
        start += 1;
    }
    
    return ans;
};