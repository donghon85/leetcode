class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        store = {}
        for ch in sentence:
            store[ch] = 1

        if len(store.keys()) == 26:
            return True
        else:
            return False