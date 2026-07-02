class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = nums.count(0)
        count_1 = nums.count(1)
        count_2 = nums.count(2)

        idx = 0

        for _ in range (count_0):
            nums[idx] = 0
            idx+=1

        for _ in range (count_1):
            nums[idx] = 1
            idx+=1

        for _ in range (count_2):
            nums[idx] = 2
            idx+=1