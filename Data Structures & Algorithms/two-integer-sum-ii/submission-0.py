class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right=len(numbers)-1
        left=0
        while right>=left:
            if numbers[right]+numbers[left]==target:
                break
            if numbers[right]+numbers[left]>target:
                right-=1
            else:
                left+=1
        return[left+1,right+1]

        