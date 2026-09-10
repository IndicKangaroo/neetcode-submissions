class Solution:
    def totalNQueens(self, n: int) -> int:
        cols=set()
        posd=set()
        negd=set()
        self.c=0
        def dfs(row):
            if row==n:
                self.c+=1
                return
            for col in range(n):
                if col not in cols and col+row not in posd and col-row not in negd:
                    cols.add(col)
                    posd.add(row+col)
                    negd.add(col-row)
                    dfs(row+1)
                    cols.remove(col)
                    posd.remove(row+col)
                    negd.remove(col-row)
        dfs(0)
        return self.c
        