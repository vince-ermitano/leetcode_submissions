class Solution:
    def decodeString(self, s: str) -> str:
        # maintain a stack pushing the characters
        # from left to right until we encounter a
        # closing bracket, in which case we will
        # pop from the stack until we reach the
        # associated opening bracket and repeat number.
        # construct the (sub)string
        # if there is still contents in the stack
        # then we know this is a nested string so we must
        # add the computed string back into the stack

        stack = []
        res = ""
        digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                # get substring to be repeated
                sub = ""
                while stack[-1] != '[':
                    sub = stack.pop() + sub
                
                # remove [
                stack.pop()

                repeat = ""
                while stack and stack[-1] in digits:
                    repeat = stack.pop() + repeat
                
                repeat = int(repeat)

                # insert back into stack if stack not empty
                if stack:
                    stack.append(sub * repeat)
                else:
                    res += sub * repeat
        
        if stack:
            res += "".join(stack)

        return res
