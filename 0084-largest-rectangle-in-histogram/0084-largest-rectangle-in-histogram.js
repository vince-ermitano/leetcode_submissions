/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    const stack = [];
    let maxArea = 0;
    
    for (let i = 0; i < heights.length; i++) {
        let start = i;
        
        while (stack.length > 0 && stack[stack.length-1][1] > heights[i]) {
            const top = stack.pop();
            maxArea = Math.max(maxArea, top[1] * (i - top[0]));
            start = top[0];
        }
        
        stack.push([start, heights[i]]);
    }
                   
    for (const item of stack) {
        maxArea = Math.max(maxArea, item[1] * (heights.length - item[0]));
    }
    
    return maxArea;
};