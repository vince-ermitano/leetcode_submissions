/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0;
    let min = 0
    
    
    for (let r = 0; r < prices.length; r++) {
        profit = Math.max(profit, prices[r] - prices[min]);
        
        if (prices[r] < prices[min]) {
            min = r;
        }
    }
    
    return profit;
};