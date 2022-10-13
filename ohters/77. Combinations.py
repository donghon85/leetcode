class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = range(1, n + 1)
        nCr = itertools.combinations(arr, k)
        return nCr