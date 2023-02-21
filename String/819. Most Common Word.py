from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        def check_str(str):
            string = ''
            for ch in paragraph.lower():
                if ch.isalpha() or ch == ' ':
                    string += ch
                else:
                    string += ' '
            return string

        string = check_str(paragraph)
        c = Counter(string.split(' '))
        ans, val = '', -1
        for str in c:
            if str not in banned and val < c[str] and str != '':
                ans = str
                val = c[str]
        return ans