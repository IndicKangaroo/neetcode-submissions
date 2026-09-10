class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board=[]
        for i in range(n):
            board.append("."*n)
        cols=set()
        posd=set()
        negd=set()
        res=[]
        def dfs(row):
            if row==n:
                res.append(list(board))
                return
            for col in range(n):
                if col not in cols and col+row not in posd and col-row not in negd:
                    cols.add(col)
                    posd.add(row+col)
                    negd.add(col-row)
                    board[row]=board[row][:col]+"Q"+board[row][col+1:]
                    dfs(row+1)
                    cols.remove(col)
                    posd.remove(row+col)
                    negd.remove(col-row)
                    board[row]=board[row][:col]+"."+board[row][col+1:]
        dfs(0)
        return res