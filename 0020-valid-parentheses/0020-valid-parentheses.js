/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    const map = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    
    for (const char of s) {
        if (!(char in map)) {
            stack.push(char);
        } else {
            if (stack.length === 0 || stack.pop() !== map[char]) return false;
        }
    }
    
    if (stack.length > 0) return false;
    return true;
};