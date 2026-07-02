class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        for i in range(n):
            if i == 0 and nums[i] > nums[i+1]:
                return i
            elif i == n-1 and nums[n-1] > nums[n-2]:
                return i
            elif nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
                
             