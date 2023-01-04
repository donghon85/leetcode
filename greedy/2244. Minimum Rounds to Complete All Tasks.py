from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        ans = 0
        for key in c:
            val = c[key]
            if val == 1:
                return -1
            ans += val // 3
            ans = ans + 1 if val % 3 > 0 else ans

        return ans