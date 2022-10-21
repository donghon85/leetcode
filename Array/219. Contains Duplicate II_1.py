class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans = False
        n = len(nums)
        con = []
        for i in range(n):
            con.append((nums[i], i))  # con = [val, idx]

        con.sort(key=lambda x: (x[0], x[1]))

        for i in range(n - 1):
            if con[i][0] == con[i + 1][0]:
                if abs(con[i][1] - con[i + 1][1]) <= k:
                    return True
        return False