/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let top = 0;
    let bottom  = matrix.length - 1;
    const COLS = matrix[0].length;
    
    while (top <= bottom) {
        const mid = Math.floor((top + bottom) / 2);
        
        if (target > matrix[mid][COLS-1]) {
            top = mid + 1;
        } else if (target < matrix[mid][0]) {
            bottom = mid - 1;
        } else {
            break;
        }
    }
    
    if (top > bottom) return false;
    
    let left = 0;
    let right = COLS-1;
    
    const potentialRow = Math.floor((top + bottom) / 2);
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (matrix[potentialRow][mid] === target) {
            return true;
        } else if (matrix[potentialRow][mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return false;
    
    
};