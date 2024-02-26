from collections import defaultdict


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = defaultdict(int)
        dp[(0, 0)] = poured
        #   dp[i,j] = dp[i-1,j-1] + dp[i-1, j]
        # or
        #   dp[i+1, j] += (dp[i,j] - 1) / 2
        #   dp[i+1, j+1] += (dp[i,j] - 1) / 2
        for i in range(query_row):
            for j in range(query_glass+1):
                excess = (dp[(i, j)] - 1)
                if excess > 0:
                    dp[(i+1, j)] += (excess/2.0)
                    dp[(i+1, j+1)] += (excess/2.0)
        print(dp)
        return dp[(query_row, query_glass)] if dp[(query_row, query_glass)] <= 1 else 1
