/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    
    if (t.length > s.length) return "";
    
    let tCounts = {};
    
    for (const c of t) {
        tCounts[c] = (tCounts[c] || 0) + 1;
    }
    
    let need = Object.keys(tCounts).length;
    
    for (const c of s.slice(0, t.length)) {
        if (c in tCounts) {
            tCounts[c] -= 1;
            
            if (tCounts[c] === 0) {
                need -= 1;
            }
        }
    }
    
    if (need === 0) return s.slice(0, t.length);
    
    let minSubstring = "";
    let minLen = Infinity;
    
    let left = 0;
    let right = t.length;
    
    while (right < s.length) {
        if (s[right] in tCounts) {
            tCounts[s[right]] -= 1;
            
            if (tCounts[s[right]] === 0) {
                need -= 1;
            }
        }
        
        
        while (need === 0 && left <= s.length - t.length) {
            if (right - left + 1 < minLen) {
                minSubstring = s.slice(left, right + 1);
                minLen = minSubstring.length;
            }
            
            if (s[left] in tCounts) {
                tCounts[s[left]] += 1;
                
                if (tCounts[s[left]] === 1) {
                    need += 1;
                }
            }
            
            left += 1;
        }
        
        right += 1;
    }
    
    return minSubstring;
};