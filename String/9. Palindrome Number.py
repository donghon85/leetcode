class Solution:
    def isPalindrome(self, x: int) -> bool:
        if abs(x) != x: return False  # remove a minus num
        x = str(x)
        n = len(str(x))

        for i in range(n // 2):
            if x[i] != x[-i - 1]:
                return False

        return True
