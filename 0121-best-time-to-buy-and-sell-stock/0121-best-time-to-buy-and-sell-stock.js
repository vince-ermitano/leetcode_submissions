/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0;
    let minVal = prices[0]
    
    
    for (let r = 0; r < prices.length; r++) {
        profit = Math.max(profit, prices[r] - minVal);
        
        if (prices[r] < minVal) {
            minVal = prices[r];
        }
    }
    
    return profit;
};