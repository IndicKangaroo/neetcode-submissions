class Solution:
    def trap(self, height: List[int]) -> int:
        pre=[0]
        m=0
        for i in range(1,len(height)-1):
            m=max(height[i-1],m)
            pre.append(m)
        m=0
        post=[0]*len(height)
        for i in range(len(height)-2,-1,-1):
            m=max(height[i+1],m)
            post[i]=m
        s=0
        for i in range(1,len(height)-1):
            s+=max(min(pre[i],post[i])-height[i],0)
        return s