class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(pos,path,total):
            if total==target:
                res.append(path[:])
                return
            if total>target:
                return
            for i in range(pos,len(candidates)):
                if i > pos and candidates[i] == candidates[i-1]:
                    continue
                if total+candidates[i]<=target:
                    path.append(candidates[i])
                    dfs(i+1,path,total+candidates[i])
                    path.pop()

        dfs(0,[],0)
        return res