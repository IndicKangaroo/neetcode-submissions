class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def dfs(pos,curr,cs):
            if pos==len(s):
                res.append(curr[:])
                return
            for i in range(pos,len(s)):
                cs = s[pos:i + 1]
                if cs==cs[::-1]:
                    curr.append(cs)
                    dfs(i+1,curr,cs)
                    curr.pop()
        dfs(0,[],"")
        return res
                
