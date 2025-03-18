class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # maintain a stack
        # iterate through asteroids
        # push asteroids going to the right onto the stack
        # when we encounter an asteroid going to the left
        # compare to the top of the stack and do the collision comparison
        # if stack is empty or top of stack is a left-directed asteroid
        # when encountering a left-directed asteroid, add to stack

        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and abs(a) > stack[-1]:
                    stack.pop()
                
                if not stack:
                    stack.append(a)
                else:
                    prev_a = stack[-1]

                    if prev_a == abs(a):
                        stack.pop()
                    elif prev_a < 0:
                        stack.append(a)
                        
                
        return stack