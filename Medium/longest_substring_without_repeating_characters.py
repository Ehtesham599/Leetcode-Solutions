# Runtime: 64ms
# Memory: 14.4 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        my_set = set()
        n = len(s)
        while (i < n and j < n):
            if s[j] not in my_set:
                my_set.add(s[j])
                j = j + 1
                ans = max(ans, j-i)
            else:
                my_set.remove(s[i])
                i = i + 1

        return ans
