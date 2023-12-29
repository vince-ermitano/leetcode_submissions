/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    const deque = [];
    const maxSlidingWindow = [];
    
    let left = 0;
    let right = 0;
    
    while (right < nums.length) {
        while (deque.length > 0 && deque[deque.length-1] < nums[right]) {
            deque.pop();
        }
        deque.push(nums[right]);
        
        if (right + 1 >= k) {
            maxSlidingWindow.push(deque[0]);
            
            if (deque[0] === nums[left]) {
                deque.shift();
            }
            
            left += 1;
        }
        
        right += 1;
    }
    
    return maxSlidingWindow;
};