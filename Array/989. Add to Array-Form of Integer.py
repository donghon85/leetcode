class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = ''.join(map(str, num))
        ans = int(num)+k
        ans = list(map(int, str(ans)))
        return ans