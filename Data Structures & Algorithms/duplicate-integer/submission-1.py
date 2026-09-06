class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
        if len(l)!=len(nums):
            return True
        else:
            return False
         