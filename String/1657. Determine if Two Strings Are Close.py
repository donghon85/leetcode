from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)

        set1 = set(word1)
        set2 = set(word2)

        sort1 = sorted(w1.values())
        sort2 = sorted(w2.values())

        return set1 == set2 and sort1 == sort2