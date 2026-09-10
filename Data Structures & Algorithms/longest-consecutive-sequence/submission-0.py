class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=set()
        maxc=0
        for i in nums:
            l.add(i)
        for i in nums:
            if i-1 not in l:
                c=1
                while True:
                    i+=1
                    if i not in l:
                        break
                    c+=1
                maxc=max(maxc,c)
        return maxc