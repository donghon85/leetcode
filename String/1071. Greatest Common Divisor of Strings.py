class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ans = ""
        s = ""
        for i in range(1, n+1):
            s = str1[:i]
            if n%i == 0 and m%i==0:
                count1, count2 = n//i, m//i
                if s * count1 == str1 and s * count2 == str2:
                    ans = s
        return ans
