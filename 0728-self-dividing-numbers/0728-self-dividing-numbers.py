class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def check(num):
            orig = num

            while (num > 1):
                lastDigit = num % 10
                num //= 10

                if lastDigit == 0:
                    return False

                if  orig % lastDigit != 0:
                    return False
            
            return True

        res = []

        for i in range(left, right + 1):
            if check(i):
                res.append(i)

        return res
            