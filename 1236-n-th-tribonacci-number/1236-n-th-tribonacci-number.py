class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        
        if n in [1, 2]:
            return 1

        num_1 = 0
        num_2 = 1
        num_3 = 1

        for i in range(n - 2):
            temp_1 = num_2
            temp_2 = num_3

            num_3 += num_1 + num_2

            num_1 = temp_1
            num_2 = temp_2
        
        return num_3
        