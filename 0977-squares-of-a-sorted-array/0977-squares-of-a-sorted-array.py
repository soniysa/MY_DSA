class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left  = 0
        right = len(nums)-1

        N_arr = [0]*len(nums)

        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left])>abs(nums[right]):
                N_arr[i] = nums[left]**2
                left+=1
            else:
                N_arr[i] = nums[right]**2
                right-=1
        return N_arr