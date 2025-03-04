class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1 for i in range(n)] for _ in range(n)]
        top = left = 0
        bottom = right = n - 1
        num = 1

        while (num <= n * n):
            for col in range(left, right + 1):
                matrix[top][col] = num
                print(num)
                num += 1
                
            for row in range(top + 1, bottom + 1):
                matrix[row][right] = num
                print(num)
                num += 1
                
            if bottom != top:
                for col in range(right - 1, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                
            if left != right:
                for row in range(bottom - 1, top, -1):
                    matrix[row][left] = num
                    num += 1

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return matrix