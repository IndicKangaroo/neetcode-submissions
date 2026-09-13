class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=1
        a=set()
        m=0
        for r in range(len(s)):
            if s[r] not in a:
                a.add(s[r])
                m=max(m,len(a))
            else:
                while s[l]!=s[r]:
                    a.remove(s[l])
                    l+=1
                a.remove(s[l])
                l+=1
                a.add(s[r])
                m=max(m,len(a))
        return m