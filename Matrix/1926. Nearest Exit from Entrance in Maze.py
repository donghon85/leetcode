class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # . is empty / + is wall
        stack = []
        visited = {}
        m, n = len(maze), len(maze[0])
        stack.append([entrance[0], entrance[1], 0])
        visited[entrance[0], entrance[1]] = True
        while stack:
            x, y, count = stack.pop(0)
            for a, b in [(1,0), (0,1), (-1,0), (0,-1)]:
                a, b = x+a, y+b
                if -1 < a < m and -1 < b < n and maze[a][b] == '.' and (a,b) not in visited:
                    visited[a,b] = True
                    if a == 0 or b == 0 or a == m-1 or b == n-1:
                        return count+1
                    else:
                        stack.append([a,b,count+1])
        return -1