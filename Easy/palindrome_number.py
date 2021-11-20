# Runtime: 68ms
# Memory: 14 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= (-2)**31 or x >= (2**31)-1:
            return False

        s = str(x)
        i = 0
        n = len(s)-1
        while i < n:
            if s[i] != s[n]:
                return False
            i = i + 1
            n = n - 1

        return True
