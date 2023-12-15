/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const map = {};
    let longest = 0;
    
    for (const num of nums) {
        map[num] = 1;
    }
    
    for (const num of nums) {
        if ((num-1) in map) continue;
        
        let currentLength = 1;
        let currentNum = num;
        
        while (currentNum+1 in map) {
            currentLength += 1;
            currentNum += 1;
        }
        
        longest = Math.max(longest, currentLength);
    }
    
    return longest;
};