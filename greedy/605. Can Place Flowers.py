class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0
        m = len(flowerbed)
        if m <= 1:
            if flowerbed[0] == 0:
                ans += 1
            return ans >= n

        for i in range(m):
            if i == 0 or i == m - 1:
                if flowerbed[i] == 0:
                    if i == 0:
                        if flowerbed[i + 1] == 0:
                            ans += 1
                            flowerbed[i] = 1
                    if i == m - 1:
                        if flowerbed[i - 1] == 0:
                            ans += 1
                            flowerbed[i] = 1
                continue
            if sum(flowerbed[i - 1:i + 2]) == 0:
                flowerbed[i] = 1
                ans += 1
        return ans >= n
