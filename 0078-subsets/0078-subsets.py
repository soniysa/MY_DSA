class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        

        self.solve(nums, 0, current,result)

        return result

    def solve(self, nums: List[int], index: int, current: List[int], result: List[List[int]]):
            if index == len(nums):
                result.append(list(current))
                return

            ## take kro
            current.append(nums[index])  
            self.solve(nums,index+1, current, result)

            # skip krdo

            current.pop()
            self.solve(nums,index+1, current, result)

           
