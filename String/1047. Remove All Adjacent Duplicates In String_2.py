class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 1: return s
        ans = []

        for ch in s:
            if len(ans) > 0 and ans[-1] == ch:
                ans.pop(-1)
            else:
                ans.append(ch)
        return ''.join(ans)