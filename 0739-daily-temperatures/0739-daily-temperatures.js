/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const stack = [];
    const ans = Array(temperatures.length).fill(0);
    
    temperatures.forEach((temp, index) => {
        
        while (stack.length > 0) {
            
            const top = stack[stack.length - 1];
            
            if (top[0] < temp) {
                ans[top[1]] = index - top[1];
                stack.pop();
            } else {
                break;
            }
        }
        
        stack.push([temp, index]);
    });
    
    return ans;
};