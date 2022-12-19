class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = {}

        for a, b in edges:
            if a in dic:
                dic[a].append(b)
            else:
                dic[a] = [b]

            if b in dic:
                dic[b].append(a)
            else:
                dic[b] = [a]

        queue = [source]
        visited = set()
        while queue:
            val = queue.pop(0)
            if val == destination:
                return True
            for dval in dic[val]:
                if dval not in visited:
                    queue.append(dval)
            visited.add(val)
        return False