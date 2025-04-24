# There are *6 ways to place a domino/tromino
# 1. Domino horizontal in which we must put another domino horizontal under it -> move two columns over
# 2. Domino vertical in which we just move to the next column
# 3. Tromino (bottom-right space open) -> move two columns over
# 4. Tromino (top-right space open) -> move two columns over
# 5. Tromino (top-left space open) -> move two columns over
#       - can only put if the prev piece was a tromino (bottom-right space open)
# 6. Tromino (bottom-left space open) -> move two columns over
#       - can only put if the prev piece was a tromino (top-right space open)
# At any column, i, we simulate placing a valid tile and add up the combinations
#   - must take note of gaps from previous tile to ensure valid tiling
# Use dp to solve each subproblem once

class Solution:
    def numTilings(self, n: int) -> int:
        
        if n == 1: return 1
        if n == 2: return 2

        # dp[i, 0] -> # of combinations that up to column i didn't produce any gaps
        # dp[i, 1] -> # of combinations that up to column i that did produce gaps
        dp = [[0, 0] for c in range(n)]
        

        dp[0] = [1, 1]
        dp[1] = [2, 2]

        for c in range(2,n):
            # explore combinations given that the previous tilings produced no gaps
            # explore vertical domino or two horizontal dominos or either of the two valid trominos
            dp[c][0] = dp[c-1][0] + dp[c-2][0] + dp[c-2][1] * 2
            # explore combinations given that the previous tilings produced gaps
            # explore horizontal domino or valid tromino
            dp[c][1] = dp[c-1][1] + dp[c-1][0]

        return dp[n-1][0] % (10**9 + 7)
            


