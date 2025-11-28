class Solution:
    def isPalindrome(self, s: str) -> bool:
        for x in s:
            if not x.isalnum():
                s = s.replace(x,"")
        s= s.lower()
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True