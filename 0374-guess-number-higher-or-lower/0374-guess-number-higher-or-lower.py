# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # binary search

        l = 1
        r = n
        num = (l + r) // 2

        while guess(num) != 0:
            if guess(num) == -1:
                r = num - 1
            else:
                l = num + 1
            
            num = (l + r) // 2
        
        return num
