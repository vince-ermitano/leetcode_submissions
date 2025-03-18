class Solution:
    def removeStars(self, s: str) -> str:
        # maintain a stack containing the non-star characters
        # iterate through s
        # if non-star char, add to stack
        # if star char, pop top of stack
        # after iterating, return resulting string

        stack = []

        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)