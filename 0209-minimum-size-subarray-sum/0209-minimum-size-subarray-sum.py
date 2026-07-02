class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        i = 0
        current_sum = 0


        for j in range(len(nums)):
            current_sum += nums[j]

            while current_sum >= target:
                min_length = min(min_length, j-i+1)
                current_sum -= nums[i]
                i+=1

        return 0 if min_length == float('inf') else min_length
