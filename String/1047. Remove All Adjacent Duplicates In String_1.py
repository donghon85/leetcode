class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 1: return s
        s = list(s)
        i = 0

        while i < len(s)-1:

            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
                i = i-1 if i > 0 else 0
                continue
            i += 1
        return ''.join(s)