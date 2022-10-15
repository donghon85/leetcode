class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for i in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:  # 맨 윗줄 초기화
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif i != 0 and j == 0:  # 맨 왼쪽 줄 초기화
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                elif i != 0 and j != 0:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]