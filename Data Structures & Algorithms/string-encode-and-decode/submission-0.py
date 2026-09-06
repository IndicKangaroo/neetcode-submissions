class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=i+",/"
        return s
    def decode(self, s: str) -> List[str]:
        l=s.split(",/")
        return l[:-1]