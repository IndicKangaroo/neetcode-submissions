class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(i,j):
            for u in range(9):
                if board[u][j]==board[i][j] and u!=i:
                    return False
                if board[i][u]==board[i][j] and u!=j:
                    return False
            for u in range(i // 3 * 3, i // 3 * 3 + 3):
                for v in range(j // 3 * 3, j // 3 * 3 + 3):
                    if (u!=i or v!=j) and board[u][v]==board[i][j]:
                        return False
            return True
        flag=0
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if not check(i,j):
                        return False
        return True