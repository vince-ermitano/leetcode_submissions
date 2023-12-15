/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const counts = {};
    const bucket = Array.from({length: nums.length + 1}, () => []);
    const ans = [];
    
    for (const num of nums) {
        counts[num] = (counts[num] || 0) + 1;
    }
    
    for (const num in counts) {
        bucket[Number(counts[num])].push(+num);
    }

    for (let i = bucket.length - 1; i >= 0; i--) {
        while (ans.length < k && bucket[i].length) {
            ans.push(bucket[i].pop());
        }
        
        if (ans.length === k) break;
    }
    
    return ans;
};