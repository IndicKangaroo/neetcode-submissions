class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=""
        for i in s:
            if i.isalnum():
                k+=i.lower()

        if k[::-1]==k:
            return True
        else:
            return False
        