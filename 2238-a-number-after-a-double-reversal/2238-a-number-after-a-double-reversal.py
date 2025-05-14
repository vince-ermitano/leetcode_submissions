class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num // 10 >= 1:
            return not num % 10 == 0
        else:
            return True