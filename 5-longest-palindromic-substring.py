class Solution:
    def expand(self, s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            #odd-size
            p1 = self.expand(s, i, i)
            if len(p1) > len(result):
                result = p1

            #even-size
            p2 = self.expand(s, i, i+1)
            if len(p2) > len(result):
                result = p2
                
        return result
