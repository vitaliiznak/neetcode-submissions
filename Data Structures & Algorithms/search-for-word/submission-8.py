from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        visited = set()
        def dfs(r, c, i):
            if i == (len(word) - 1) and board[r][c] == word[i]:
                return True

            if board[r][c] != word[i] or ((r,c) in visited):
                return False

     

        
       

            visited.add((r, c))
            
            return (
                (r-1 >= 0 and dfs(r-1, c, i+1)) or
                (r+1 < ROWS and dfs(r+1, c, i+1)) or
                (c-1 >= 0 and dfs(r, c-1, i+1)) or
                (c+1 < COLS and dfs(r, c+1, i+1))
            )

            visited.remove((r, c))

                
        return any(
            board[r][c] == word[0] and dfs(r, c, 0)
            for r in range(ROWS)
            for c in range(COLS)
        )
        
        



            

            

        














