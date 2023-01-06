class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        ans = 0
        for cost in costs:
            if cost <= coins:
                ans += 1
                coins -= cost
        return ans