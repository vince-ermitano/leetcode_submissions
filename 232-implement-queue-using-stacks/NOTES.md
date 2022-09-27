# Notes

## Idea
* Maintain one stack as the in-order stack and the other as a normal stack.
* Whenever popping/peeking we can simply get the top element in the in-order stack if it isn't empty.
* If it is empty, that means the element we want is at the bottom of the normal stack, so we push all the elements in the normal stack to the in-order stack in the order we pop them so that the in-order stack maintains its in-order property.
* We can then pop/peek from the in-order stack

## Complexity
* Time complexity is *O(1)* for a push operation, *O(1)* AMORTIZED peek/pop operation since we will only have to move the elements from the normal stack to the in-order stack when the in-order stack is empty.
* Space complexity is *O(N)* to store all the elements in the stacks.
