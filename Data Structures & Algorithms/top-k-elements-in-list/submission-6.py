class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in d:
            l.append([i,d[i]])
        res=[]
        for i in range(k):
            m=0
            ind=None
            for i in l:
                if i[1]>m:
                    m=i[1]
                    ind=i[0]
            res.append(ind)
            l.remove([ind,m])
        return res





        

        