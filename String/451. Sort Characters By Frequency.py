from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        items = []
        ans = ""
        for key in c:
            items.append([key, c[key]])
        items.sort(key=lambda x: x[1], reverse=True)

        for key, val in items:
            ans += key * val
        return ans