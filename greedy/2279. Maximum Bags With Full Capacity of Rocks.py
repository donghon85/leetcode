class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)
        ans = 0
        rest = []
        for i in range(n):
            if capacity[i] == rocks[i]:
                ans += 1
            else:
                rest.append(capacity[i]- rocks[i])
        rest.sort()
        while additionalRocks > 0 and rest:
            val = rest.pop(0)
            if val <= additionalRocks:
                additionalRocks -= val
                ans += 1

        return ans