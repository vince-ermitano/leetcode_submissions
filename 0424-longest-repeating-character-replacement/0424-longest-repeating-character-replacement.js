/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let maxf = 0;
    let map = {};
    let left = 0;
    let longest = 0;
    
    for (let right = 0; right < s.length; right++) {
        map[s[right]] = s[right] in map ? map[s[right]] + 1 : 1;
        maxf = Math.max(maxf, map[s[right]]);
        
        while (right - left + 1 - maxf > k) {
            map[s[left]] -= 1
            left += 1;
        }
        
        longest = Math.max(longest, right - left + 1);
        
    }
    
    return longest;
};