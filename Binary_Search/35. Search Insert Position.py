class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] == target or nums[i] > target:
                break

        return i+1 if nums[n-1] < target else i

    def searchInsert2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return left