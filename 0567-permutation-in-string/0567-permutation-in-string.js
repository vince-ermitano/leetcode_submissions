/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    
    if (s2.length < s1.length) return false;
    
    
    let s1_counts = {};
    
    for (const c of s1) {
        s1_counts[c] = (s1_counts[c] || 0) + 1;
    }
    
    let need = Object.keys(s1_counts).length;
    let left = 0
    let right = 0;
    
    while (right < s2.length) {
        if (s2[right] in s1_counts) {
            s1_counts[s2[right]] -= 1;
            if (s1_counts[s2[right]] === 0) {
                need -= 1;
            } else if (s1_counts[s2[right]] === -1) {
                need += 1;
            }
        }
        
        if (need === 0) return true;
        
        if (right - left + 1 === s1.length) {
            
            if (s2[left] in s1_counts) {
                s1_counts[s2[left]] += 1
                
                if (s1_counts[s2[left]] === 0) {
                    need -= 1;
                } else if (s1_counts[s2[left]] === 1) {
                    need += 1;
                }
            }
            
            left += 1;
        }
        
        right += 1;
    }
    return false;
};