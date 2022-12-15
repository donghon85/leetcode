class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # note mem[i][j] = mem[i-1][j-1]+1 if text1[i] == text2[j] else max(mem[i-1][j], mem[i][j-1])
        n, m = len(text1), len(text2)
        mem = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    mem[i+1][j+1] = mem[i][j]+1
                else:
                    mem[i+1][j+1] = max(mem[i+1][j], mem[i][j+1])
        return max(max(row) for row in mem)