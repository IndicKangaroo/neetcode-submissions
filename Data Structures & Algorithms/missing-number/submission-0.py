class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=0
        for i in range(1,len(nums)+1):
            x=x^i
        for i in range(len(nums)):
            x=x^nums[i]
        return x
        