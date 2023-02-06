from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic_p = Counter(p)
        ans = []
        for i in range(len(s)-len(p)+1):
            temp = Counter(s[i:i+len(p)])
            if dic_p == temp:
                ans.append(i)
        return ans
