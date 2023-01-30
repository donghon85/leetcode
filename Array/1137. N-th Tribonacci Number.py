class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0, 1, 1]

        for i in range(2, n):
            ans.append(sum(ans[i - 2:i + 1]))

        return ans[n]