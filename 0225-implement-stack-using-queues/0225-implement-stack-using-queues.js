
var MyStack = function() {
    this.q1 = [];
    this.q2 = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    this.q1.push(x);
    
    let size = this.q2.length;
    
    while (size > 0) {
        this.q1.push(this.q2.shift());
        size--;
    }
    
    [this.q1, this.q2] = [this.q2, this.q1]
    
    console.log(this.q2);
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function() {
    return this.q2.shift();
};

/**
 * @return {number}
 */
MyStack.prototype.top = function() {
    return this.q2[0];
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    return this.q2.length === 0;
};

/** 
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */