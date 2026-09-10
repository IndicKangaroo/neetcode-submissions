class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                l.append(i)
            elif i==")":
                if len(l)==0 or l[-1]!="(":
                    return False
                else:
                    l.pop()
            elif i=="]":
                if len(l)==0 or l[-1]!="[":
                    return False
                else:
                    l.pop()
            elif i=="}":
                if len(l)==0 or l[-1]!="{":
                    return False
                else:
                    l.pop()
        if len(l)!=0:
            return False
        return True
