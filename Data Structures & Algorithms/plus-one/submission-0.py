class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=0
        for i in range(len(digits)):
            l+=digits[i]*(10**(len(digits)-i-1))
        l+=1
        res=[]
        for i in str(l):
            res.append(i)
        return res