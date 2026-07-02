class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            needed = 0
            for pile in piles:
                needed += (pile + mid - 1) // mid

            if needed <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans