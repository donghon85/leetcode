class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0]*n
        dp[0] = 1

        for i in range(n):
            if dp[-1] == 1: return True

            elif dp[i] == 1:
                dp[i:i+nums[i]+1] = [1]*(nums[i]+1)
        return dp[-1] == 1