/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  function roundTowardsZero(number) {
    return Math.sign(number) * Math.floor(Math.abs(number));
  }

  const stack = [];

  for (const token of tokens) {
    if (token === "+") {
      stack.push(stack.pop() + stack.pop());
    } else if (token === "-") {
      stack.push(-stack.pop() + stack.pop());
    } else if (token === "*") {
      stack.push(stack.pop() * stack.pop());
    } else if (token === "/") {
      const divisor = stack.pop();
      const dividend = stack.pop();
      stack.push(roundTowardsZero(dividend / divisor));
    } else {
      stack.push(Number(token));
    }
  }

  return stack[0];
};