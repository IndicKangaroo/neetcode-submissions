class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def dfs(pos1, pos2):
            if pos1 == len(s):
                return True

            if pos2 == len(t):
                return False

            if s[pos1] == t[pos2]:
                return dfs(pos1 + 1, pos2 + 1)

            return dfs(pos1, pos2 + 1)

        return dfs(0, 0)