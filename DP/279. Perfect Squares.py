class Solution:
    def numSquares(self, n: int) -> int:
        square = [inf for _ in range(n+1)]

        for i in range(n+1):
            if i*i < n+1:
                square[i*i] = 1

        for i in range(n+1):
            if square[i] > 1:
                m = inf
                for j in range(1, n+1):
                    if j*j > i:
                        break
                    if square[i-j*j] < m:
                        m = square[i-j*j]
                    if m == 1:
                        break
                square[i] = m+1
        return square[n]