class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        m = len(strs)
        n = len(strs[0])
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(strs[j][i])
            if temp != sorted(temp): ans +=1
        return ans