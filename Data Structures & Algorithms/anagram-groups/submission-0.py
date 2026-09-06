class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        res=[]
        for i in strs:
            a=[0]*26
            for j in i:
                a[ord(j)-ord("a")]+=1
            if tuple(a) in d:
                d[tuple(a)].append(i)
            else:
                d[tuple(a)]=[i]
        for i in d:
            res.append(d[i])
        return res
			

        