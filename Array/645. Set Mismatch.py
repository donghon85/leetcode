class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        re = loss = 0
        for i in range(1, len(nums) + 1):
            if c[i] == 2:
                re = i
            if c[i] == 0:
                loss = i

        return [re, loss]