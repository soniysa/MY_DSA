class Solution:

    def solve(self, nums: List[int], permutation, myset, result):

        if len(permutation) == len(nums):
            result.append (list(permutation))
            return


        for i in range(0, len(nums)):
            if nums[i] not in myset:
                myset.add(nums[i])
                permutation.append(nums[i])
                self.solve(nums, permutation, myset, result)
                myset.remove(nums[i]) 
                permutation.pop()## kyoki hamesha last se hi remove krna tha

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        myset = set()
        self.solve(nums, permutation, myset, result)
        return result