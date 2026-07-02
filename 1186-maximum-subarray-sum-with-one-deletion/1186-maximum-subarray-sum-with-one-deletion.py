class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return arr[0]

        left = [0]*n
        right = [0]*n

        left[0] = arr[0]

        for i in range(1, n):
            left[i] = max(arr[i], left[i-1] + arr[i])

        right[n-1] = arr[n-1]

        for i in range(n-2, -1, -1):
            right[i] = max(arr[i], right[i+1] + arr[i])

        ans = max(left)

        for i in range(1, n - 1):
            ans = max(ans, left[i - 1] + right[i + 1])

        return ans