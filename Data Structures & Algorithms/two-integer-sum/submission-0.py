class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        l.append(i)
                        l.append(j)
                        return l

        



        