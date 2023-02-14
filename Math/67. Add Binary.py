class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def btoi(nums):
            ans = 0
            k = 1
            for num in nums:
                ans += k * int(num)
                k *= 2
            return ans
        ans = btoi(a[::-1]) + btoi(b[::-1])
        return bin(ans)[2:]
