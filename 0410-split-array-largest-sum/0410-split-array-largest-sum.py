class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        ans = -1
        while low <= high:
            mid = (low+high)//2

            subarrays = 1
            currSum = 0

            for num in nums:

                if currSum + num <= mid:
                    currSum += num
                else:
                    subarrays += 1
                    currSum = num

            if subarrays <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans