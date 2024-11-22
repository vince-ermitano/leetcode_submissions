/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    
    /* if n is in fact a power of two, subtracting 1 from its binary form will cause all the 0's to the right of the 1 bit from 1 will turn to 1's.
        Thus the resulting binary number will have 0's where the original binary number has 1's and will have 1's where the original has 0's. We can then
        just check if the resulting bitwise & operation between the two numbers results in 0 to confirm that it's a power of 2.
        */
    
    return n > 0 && (n & (n-1)) === 0;
};