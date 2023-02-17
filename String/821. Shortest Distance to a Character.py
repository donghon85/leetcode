class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0 for _ in range(n)]
        c_idx = [i for i in range(n) if s[i] == c]
        cur, m = 0, len(c_idx)
        for i in range(n):
            if cur < m - 1 and abs(i - c_idx[cur]) > abs(i - c_idx[cur + 1]):
                cur += 1
            ans[i] = abs(i - c_idx[cur])

        return ans
