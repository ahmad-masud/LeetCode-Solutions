class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()

            for i in range(9):
                if board[r][i] == ".": 
                    continue

                if board[r][i] in seen:
                    return False
                
                seen.add(board[r][i])
        
        for c in range(9):
            seen = set()

            for i in range(9):
                if board[i][c] == ".":
                    continue

                if board[i][c] in seen:
                    return False
                
                seen.add(board[i][c])
            
        for b in range(9):
            seen = set()

            for i in range(3):
                for j in range(3):
                    r = (b // 3) * 3 + i
                    c = (b % 3) * 3 + j

                    if board[r][c] == ".":
                        continue

                    if board[r][c] in seen:
                        return False
                    
                    seen.add(board[r][c])

        return True