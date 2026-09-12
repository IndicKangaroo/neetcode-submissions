class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(pos, path):
            if pos == len(nums):
                res.append(path[:])
                return

            dfs(pos + 1, path)

            path.append(nums[pos])
            dfs(pos + 1, path)
            path.pop()

        dfs(0, [])
        return res