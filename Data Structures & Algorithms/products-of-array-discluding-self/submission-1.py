class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        pro=1
        for i in range(len(nums)):
            pre.append(pro)
            pro=pro*nums[i]
        post=[] 
        pro=1
        for i in range(len(nums)-1,-1,-1):
            post.append(pro)
            pro=pro*nums[i]
        res=[]
        for i in range(len(nums)):
            res.append(pre[i]*post[len(nums)-i-1])
        return res