class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic, mem = {0:-1}, 0
        for i, num in enumerate(nums):
            if k != 0:
                mem = (mem + num) % k
            else:
                mem += num
            if mem not in dic:
                dic[mem] = i
            else:
                if i -dic[mem] >= 2:
                    return True
        return False