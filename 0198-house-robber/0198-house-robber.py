class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def solve(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            take = nums[i] + solve(i+2)
        
            skip = solve(i+1)
        
            memo[i] = max(take, skip)
            return memo[i]
        return solve(0)
        
            
