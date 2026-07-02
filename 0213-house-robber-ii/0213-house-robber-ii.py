class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(arr):
            memo = {}
            def solve(i):

                if i in memo:
                    return memo[i]
                
                if i >= len(arr):
                    return 0

                take = arr[i] + solve(i+2)
                skip = solve(i+1)

                memo[i] = max(take, skip) 
                return memo[i]

            return solve(0)

        return max(
            rob1(nums[:-1]),
            rob1(nums[1:])
        )