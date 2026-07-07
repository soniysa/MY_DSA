# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:

    def applybinaryAscending(self, mountainArr, target, low, high)-> int:
        while low <= high:
            mid = low + (high-low)//2

            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                low = mid + 1
            else: 
                high = mid - 1

        return -1

    def applybinarydescending(self, mountainArr, target, low, high)-> int:
        while low <= high:
            mid = low + (high-low)//2

            if mountainArr.get(mid) == target:
                return mid
            
            elif mountainArr.get(mid) < target:
                high = mid-1
            else: 
                low = mid+1

        return -1


    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        low = 0
        high = n - 1 

        while(low < high):
            mid = low + (high - low )//2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                low = mid+1
            else:
                high = mid

        peak = low

        ans = self.applybinaryAscending(mountainArr, target, 0, peak)

        if ans != -1:
            return ans
        
        ans = self.applybinarydescending(mountainArr, target, peak+1, n-1)

        return ans

        