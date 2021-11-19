# Runtime: 16ms
# Memory usage: 13.4 MB
class Solution(object):
    def reverse(self, x):
        res = int(str(abs(x))[::-1])
        if res >= (2**31)-1 or res <= (-2)**31:
            return 0

        if x < 0:
            return res*-1
        else:
            return res
