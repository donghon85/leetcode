class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        c_items = list(c.items())
        c_items.sort(key=lambda x: (-x[1], x[0]))

        ans = []
        for i in range(k):
            ans.append(c_items[i][0])
        return ans