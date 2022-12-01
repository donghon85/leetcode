from collections import Counter
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        # the first solution
        n = len(s)//2
        a = Counter(s[:n])
        b = Counter(s[n:])
        vowels_anum, vowels_bnum = 0, 0
        for v in vowels:
            vowels_anum += a[v]
            vowels_bnum += b[v]
        return True if vowels_anum == vowels_bnum else False

        # the second solution
        # n = len(s)
        # aa, bb =0, 0
        # for i in range(n):
        #     if i < n//2:
        #         if s[i] in vowels:
        #             aa+=1
        #     else:
        #         if s[i] in vowels:
        #             bb += 1
        # return True if aa == bb else False