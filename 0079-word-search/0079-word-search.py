class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        cols = len(board[0])


        for i in range(0,row):
            for j in range(0,cols):
                if board[i][j] == word[0] and self.findWord(board,word,0,i,j):
                    return True


        
        return False;

    def findWord(self, board: List[List[str]], word: str, idx, i, j) -> bool:

        if len(word) == idx:
            return True

        if(i<0 or j<0 or i >= len(board) or j >= len(board[0]) or board[i][j]!= word[idx]):
            return False
        
        temp  = board[i][j]
        board[i][j] = '$'

        # left
        
        left = self.findWord(board, word, idx+1, i, j-1)
        if(left == True):
            return True

        # right
        
        right = self.findWord(board, word, idx+1, i, j+1)
        if(right == True):
            return True
        
        # Top
        
        Top = self.findWord(board, word, idx+1, i-1, j)
        if(Top == True):
            return True

        # Bottom
        
        Bottom = self.findWord(board, word, idx+1, i+1, j)
        if(Bottom == True):
            return True

        board[i][j] = temp
        return False