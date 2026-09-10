class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        mem={}
        def dfs(pos1,pos2):
            if pos1==len(s):
                return True
            if pos2==len(t):
                return False
            if s[pos1]==t[pos2]:
                if (pos1+1,pos2+1) in mem:
                    return mem[(pos1+1,pos2+1)]
                else:
                    mem[(pos1+1,pos2+1)]=dfs(pos1+1,pos2+1)
                    return mem[(pos1+1,pos2+1)]
            else:
                if (pos1,pos2+1) in mem:
                    return mem[(pos1,pos2+1)]
                else:
                    mem[(pos1,pos2+1)]=dfs(pos1,pos2+1)
                    return mem[(pos1,pos2+1)]
            return False
        return dfs(0,0)

        