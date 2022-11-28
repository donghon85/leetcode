class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[], []]
        dic = {}
        for w, l in matches:
            if w not in dic:
                dic[w] = 0
            if l not in dic:
                dic[l] = 1
            else:
                dic[l] = dic[l] + 1
        result = list(dic.items())
        result.sort(key=lambda x: x[0])

        for i in range(len(result)):
            if result[i][1] == 0:
                ans[0].append(result[i][0])
            if result[i][1] == 1:
                ans[1].append(result[i][0])
        return ans