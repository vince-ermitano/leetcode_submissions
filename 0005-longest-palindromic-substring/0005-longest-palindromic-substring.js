/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    
    function expand(left, right, str) {
        while (left >= 0 && right < str.length && str[left] === str[right]) {
            left -= 1;
            right += 1;
        }

        return [left + 1, right - 1, right - left - 1];
    }

    let left = 0;
    let right = 0;
    let longest = 0;
    
    for (let i = 0; i < s.length; i++) {
        let oddExpansion = expand(i, i, s);
        let evenExpansion = expand(i, i+1, s);

        if (oddExpansion[2] > longest) {
            left = oddExpansion[0];
            right = oddExpansion[1];
            longest = oddExpansion[2];
        }
        
        if (evenExpansion[2] > longest) {
            left = evenExpansion[0];
            right = evenExpansion[1];
            longest = evenExpansion[2];
        }
    }

    return s.substring(left, right + 1);
};