class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        ans = []
        for word in words:
            temp = []
            for i in range(len(word)):
                temp.append(dic[word[i]])
            ans.append(temp)
        return ans == sorted(ans)