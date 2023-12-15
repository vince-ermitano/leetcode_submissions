/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const groups = {};
    
    strs.forEach(str => {
        const counts = Array(26).fill(0);
        
        for (const char of str) {
            counts[char.charCodeAt(0) - 97] += 1
        }
        
        // const key = counts.join(',');
        
        if (!groups[counts]) {
            groups[counts] = [];
        }
        groups[counts].push(str);
    });
    
    return Object.values(groups);
};