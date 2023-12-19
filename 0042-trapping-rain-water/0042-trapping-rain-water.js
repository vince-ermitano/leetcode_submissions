/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let left = 0;
    let right = height.length - 1;
    let maxLeftHeight = height[left];
    let maxRightHeight = height[right];
    let waterTrapped = 0;
    
    while (left < right) {
        if (maxLeftHeight <= maxRightHeight) {
            left += 1;
            maxLeftHeight = Math.max(maxLeftHeight, height[left]);
            waterTrapped += maxLeftHeight - height[left];
        } else {
            right -= 1;
            maxRightHeight = Math.max(maxRightHeight, height[right]);
            waterTrapped += maxRightHeight - height[right];
        }
    }
    
    return waterTrapped;
};