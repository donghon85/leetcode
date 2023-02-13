class Solution:
    def jump(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        cur, curFar = 0, 0

        for i in range(n-1):
            curFar = max(curFar, nums[i] + i)

            if i == cur:
                cur = curFar
                ans += 1
        return ans