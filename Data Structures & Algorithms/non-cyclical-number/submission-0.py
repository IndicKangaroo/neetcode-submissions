class Solution:
    def isHappy(self, n: int) -> bool:
        l=set()
        s=0
        while True:
            for i in str(n):
                s+=int(i)*int(i)
            if s in l:
                return False
            if s==1:
                return True
            else:
                l.add(s)
            n=s
            s=0