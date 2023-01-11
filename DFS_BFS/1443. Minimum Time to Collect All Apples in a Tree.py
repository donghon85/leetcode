class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        path = {}

        for a, b in edges:
            if a not in path:
                path[a] = [b]
            else:
                path[a].append(b)
            if b not in path:
                path[b] = [a]
            else:
                path[b].append(a)

        def dfs(node, parent):
            ans = 0
            for i in path[node]:
                if i != parent:
                    ans += dfs(i, node)

            if ans != 0 or hasApple[node]:
                ans += 2

            return ans

        return max(dfs(0, -1)-2, 0)