class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u', 'A','O','I','U','E'}
        s = list(s)
        order = []
        for ch in s:
            if ch in vowels:
                order.append(ch)
        ans =""
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = order.pop()
            ans += s[i]
        return ans
