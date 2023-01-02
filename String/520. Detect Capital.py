class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word: return True

        if word.lower() == word: return True

        temp = list(word)
        if len(word) > 1 and temp[0].upper() + word[1:].lower() == word: return True

        return False