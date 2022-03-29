class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board[0])
        m = len(board)
        p = len(word)
        
        def helper(r, c, pos):
            if pos >= p:
                return True
            elif 0 <= r < m and 0<=c<n and board[r][c] == word[pos]:
                temp = board[r][c]
                board[r][c] = None
                if helper(r-1, c, pos+1) or helper(r+1, c, pos+1) or helper(r, c-1, pos+1) or helper(r, c+1, pos+1):
                    return True
                board[r][c] = temp
                return False
        for i in range(m):
            for j in range(n):
                if helper(i, j, 0):
                    return True
        return False