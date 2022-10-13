class Solution:
    def isHappy(self, n: int) -> bool:
        val = 0
        check = {}
        while val != 1:
            val = 0
            temp = list(str(n))

            for i in range(len(temp)):
                val += int(temp[i]) * int(temp[i])

            if n not in check:
                check[n] = 1
                n = val
            else:
                return False
        return True

