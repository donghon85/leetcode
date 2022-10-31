class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):  # 세로 진행
            x = i
            y = 0
            prev = matrix[x][y]
            for j in range(m):
                if 0 <= x < m and 0 <= y < n:
                    if prev != matrix[x][y]:
                        return False
                else:
                    break
                x, y = x + 1, y + 1

        for i in range(1, n):
            x = 0
            y = i
            prev = matrix[x][y]
            for j in range(m):
                if 0 <= x < m and 0 <= y < n:
                    if prev != matrix[x][y]:
                        return False
                else:
                    break
                x, y = x + 1, y + 1

        return True
