class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        queue = [val for val in rooms[0]]
        visited = set()
        visited.add(0)

        while queue:
            val = queue.pop(0)

            if val not in visited:
                for v in rooms[val]:
                    queue.append(v)

                visited.add(val)
        return True if n == len(visited) else False