class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = []
        for q in queries:
            sum = 0
            count = 0
            for i in range(n):
                if sum+nums[i] <= q:
                    sum += nums[i]
                    count += 1
                else:
                    break
            ans.append(count)
        return ans