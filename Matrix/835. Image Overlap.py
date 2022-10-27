class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        import numpy as np
        n = len(img1)

        img1, img2 = np.array(img1), np.array(img2)
        pad = np.pad(img1, n, mode='constant', constant_values=(0, 0))
        ans, pad_n = 0, len(pad)

        for x in range(pad_n - n):
            for y in range(pad_n - n):
                temp_pad = pad[x:x + n, y:y + n]
                temp_ans = np.sum(temp_pad * img2)
                ans = max(ans, temp_ans)
        return ans