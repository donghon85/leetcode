class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n, i = len(nums), 0
        while i < n-1:
            if nums[i] == nums[i+1]:
                nums.append(nums.pop(i+1))
                print(nums[i], i)
                n -= 1
                continue
            i += 1
        return n
