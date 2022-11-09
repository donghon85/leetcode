class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sum_list = [0] * n
        sum_list[0] = nums[0]
        for i in range(1, n):
            sum_list[i] += sum_list[i-1] + nums[i]

        for i in range(len(nums)):
            left = sum_list[i] - nums[i]
            right = sum_list[-1] - sum_list[i]
            if left == right:
                return i
        return -1