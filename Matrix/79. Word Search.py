class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, k = len(board), len(board[0]), len(word)

        def backtrack(x, y, w, visited):
            if board[x][y] == word[w]:
                if w == k - 1:
                    return True

                for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = x + a, y + b
                    if -1 < nx < m and -1 < ny < n and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        if backtrack(nx, ny, w + 1, visited): return True
                        visited.remove((nx, ny))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0, {(i, j)}): return True

        return False
