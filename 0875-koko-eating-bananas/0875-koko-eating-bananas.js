/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    let left = 0;
    let right = Math.max(...piles);
    let ans = right;
    
    while (left <= right) {
        const k = Math.floor((left + right) / 2);
        
        let hours = 0;
        
        for (const p of piles) {
            hours += Math.ceil(p / k);
        }
        
        if (hours <= h) {
            ans = Math.min(k, ans);
            right = k - 1;
        } else {
            left = k + 1;
        }
    }
    
    return ans;
};