class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        cols = len(mat[0])

        for i in range(row):
            for j in range(cols):

                up = float("-inf")
                down = float("-inf")
                left = float("-inf")
                right = float("-inf")

                if i > 0:
                    up = mat[i-1][j]
                if i < row -1:
                    down = mat[i+1][j]
                if j >0:
                    left = mat[i][j-1]
                if j < cols-1:
                    right = mat[i][j+1]

                if (mat[i][j] > up and
                   mat[i][j] > down and
                   mat[i][j] > left and
                   mat[i][j] > right):
                   return [i,j]