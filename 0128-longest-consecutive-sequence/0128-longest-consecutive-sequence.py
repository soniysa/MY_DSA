class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_map = {}
        for num in nums:
            num_map[num] = False
        for key in num_map:
            if (key - 1) not in num_map:
                num_map[key] = True

        ans = 0

        for key in num_map:
            if num_map[key]:
                k = 1
                while (key + k) in num_map:
                    k += 1

                ans = max(k, ans) 

        return ans       


        
