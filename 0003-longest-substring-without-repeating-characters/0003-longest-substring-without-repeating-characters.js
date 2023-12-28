/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let longest = 0;
    let left = 0;
    const map = {};
    
    for (let right = 0; right < s.length; right++) {
        while (s[right] in map) {
            delete map[s[left]];
            left += 1;
        }
        map[s[right]] = 1;
        longest = Math.max(longest, right - left + 1);
    }
    
    return longest;
    
};