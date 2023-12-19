/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const stack = [];
    const res = [];
    
    const backtrack = (openCount, closedCount) => {
        if (openCount === closedCount && openCount === n) {
            res.push(stack.join(''));
        }
        
        if (openCount < n) {
            stack.push('(');
            backtrack(openCount + 1, closedCount);
            stack.pop();
        }
        
        if (closedCount < openCount) {
            stack.push(')');
            backtrack(openCount, closedCount + 1);
            stack.pop();
        }
    }
    
    backtrack(0, 0);
    
    return res;
};