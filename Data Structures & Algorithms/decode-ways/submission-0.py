class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(pos):
            if pos == len(s):
                return 1

            if s[pos] == '0':
                return 0

            if pos in memo:
                return memo[pos]

            ans = dfs(pos + 1)

            if pos + 1 < len(s) and 10 <= int(s[pos:pos + 2]) <= 26:
                ans += dfs(pos + 2)

            memo[pos] = ans
            return ans

        return dfs(0)