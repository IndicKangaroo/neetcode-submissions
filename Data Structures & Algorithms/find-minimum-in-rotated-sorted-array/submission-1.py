class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif nums[0]<nums[len(nums)-1]:
            return nums[0]
        else:
            low=0
            high=len(nums)-1
            while low<high:
                mid=low+(high-low)//2
                if(nums[mid]<nums[mid-1] and mid>0):
                    return nums[mid]
                elif(nums[mid]>nums[mid+1] and mid<len(nums)-1):
                    return nums[mid+1]
                else:
                    if nums[mid]<nums[high]:
                        high=mid-1
                    else:
                        low=mid+1

        