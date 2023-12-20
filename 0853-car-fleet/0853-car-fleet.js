/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    const zipped = position.map((pos, index) => {
        return [pos, speed[index]];
    })
    
    zipped.sort((a, b) => {
        return b[0] - a[0];
    });
    
    const stack = [];
    
    for (const car of zipped) {
        
        const timeToArrive = (target - car[0]) / car[1]; 
        if (stack.length === 0 || timeToArrive > stack[stack.length-1]) {
            stack.push(timeToArrive);
        }
    }
    
    console.log(stack);
    
    return stack.length;
};