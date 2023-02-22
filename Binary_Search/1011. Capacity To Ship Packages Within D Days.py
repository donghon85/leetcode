class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left <= right:
            mid = (left + right) // 2
            temp_day = 1
            temp_w = 0

            for w in weights:
                temp_w += w
                if temp_w > mid:
                    temp_day += 1
                    temp_w = w

            if temp_day > days:
                left = mid + 1
            else:
                right = mid - 1
        return left