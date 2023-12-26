
var TimeMap = function() {
    this.map = {};
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    if (!(key in this.map)) this.map[key] = [];
    
    this.map[key].push([value, timestamp]);
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    let value = "";
    
    const values = this.map[key];
    
    if (values === undefined) return value;
    
    let left = 0;
    let right = values.length-1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (values[mid][1] <= timestamp) {
            value = values[mid][0];
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return value;
};

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */