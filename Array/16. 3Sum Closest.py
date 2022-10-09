class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        n = len(nums)
        nums.sort()
        for i in range(n):
            j, k = i + 1, n - 1

            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                ans = cur if abs(target - cur) < abs(target - ans) else ans

                if cur < target:
                    j += 1
                else:
                    k -= 1
        return ans