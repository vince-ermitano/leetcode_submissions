/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const counts = {};
    
    for (const char of s) {
        counts[char] = (counts[char] || 0) + 1;
    }
    
    for (const char of t) {
        if (!counts[char]) {
            return false;
        }
        counts[char] -= 1
    }
    
    for (const count of Object.values(counts)) {
        if (count !== 0) {
            return false;
        }
    }
    
    return true;
};