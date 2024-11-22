/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    
    if (n < 1) return false
    else if (n == 1) return true;
    else return isPowerOfTwo(n/2);
};