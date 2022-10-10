class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = list(palindrome)
        n = len(s)

        for i in range(n):
            if s[i] > 'a':
                if n % 2 == 0 or i != n // 2:
                    s[i] = 'a'
                    return ''.join(s)

        if n > 1:
            s[-1] = 'b'
            return ''.join(s)
        return ''