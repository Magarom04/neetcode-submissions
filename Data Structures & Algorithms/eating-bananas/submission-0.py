import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canFinish(speed):
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / speed)
            return total_hours <= h

        left = 1
        right = max(piles)

        answer = right

        while left <= right:
            mid = (left + right) // 2

            if canFinish(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
