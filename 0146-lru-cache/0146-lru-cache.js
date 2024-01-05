var Node = function(key = 0, val = 0) {
    this.key = key;
    this.val = val;
    this.prev = null;
    this.next = null;
}


/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.map = new Map();
    this.capacity = capacity;
    
    this.leastRecent = new Node();
    this.mostRecent = new Node();
    
    this.leastRecent.next = this.mostRecent;
    this.mostRecent.prev = this.leastRecent;
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if (this.map.has(key)) {
        this.remove(this.map.get(key));
        this.insert(this.map.get(key));
        return this.map.get(key).val;
    }
    return -1;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (this.map.has(key)) {
        this.remove(this.map.get(key));
    }
    
    this.map.set(key, new Node(key, value));
    this.insert(this.map.get(key));
    
    if (this.map.size > this.capacity) {
        let lru = this.leastRecent.next;
        this.remove(lru);
        delete this.map.delete(lru.key);
    }
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

LRUCache.prototype.remove = function(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
}

LRUCache.prototype.insert = function(node) {
    let next = this.mostRecent;
    let prev = this.mostRecent.prev;
    node.next = next;
    node.prev = prev;
    next.prev = node;
    prev.next = node;
}