class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # maintain a stack
        # iterate through asteroids
        # push asteroids going to the right onto the stack
        # when we encounter an asteroid going to the left
        # compare to the top of the stack and do the collision comparison
        # until asteroid stops colliding
        # if stack is empty or top of stack is a left-directed asteroid,
        # add to stack

        stack = []


        for a in asteroids:
            # add right-directed asteroids
            if a > 0:
                stack.append(a)

            # encounter left-directed asteroid
            else:
                # destroy prev asteroids as long as curr asteroid is larger
                while stack and stack[-1] > 0 and abs(a) > stack[-1]:
                    stack.pop()
                
                # if not more asteroids just add curr asteroid
                if not stack:
                    stack.append(a)

                # handle case where prev asteroid is either
                # same size as curr asteroid,
                # a left-directed asteroid,
                # or larger than the curr asteroid
                else:
                    prev_a = stack[-1]

                    if prev_a == abs(a):
                        stack.pop()
                    elif prev_a < 0:
                        stack.append(a)
                        
                
        return stack