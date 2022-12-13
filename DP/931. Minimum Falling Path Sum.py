class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[inf]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                    continue
                for p in [(-1, -1), (-1, 0), (-1, 1)]:
                    nx, ny = i+p[0], j+p[1]
                    if 0 <= nx < m and 0 <= ny < n:
                        dp[i][j] = min(dp[i][j],  dp[nx][ny]+matrix[i][j])
        # print(dp)
        return min(dp[-1])