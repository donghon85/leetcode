class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        ans = 0

        for i in range(1, len(colors)):
            if colors[i - 1] == colors[i]:
                if neededTime[i - 1] < neededTime[i]:
                    ans += neededTime[i - 1]
                else:
                    ans += neededTime[i]
                    neededTime[i] = neededTime[i - 1]
        return ans
