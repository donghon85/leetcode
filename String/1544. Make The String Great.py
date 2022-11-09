class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s) -1 :
            if (s[i] == s[i+1].lower() and s[i].upper() == s[i+1]) or (s[i] == s[i+1].upper() and s[i].lower() == s[i+1]):
                s.pop(i)
                s.pop(i)
                i = 0
                continue
            i += 1
        return "".join(s)