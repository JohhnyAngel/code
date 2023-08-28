class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        L = len(s)
        next = [0]*L
        j = 0
        for i in range(1, len(s)):
            while s[i] != s[j] and j > 0:
                j = next[j-1]
            if s[j] == s[i]:
                j += 1
            next[i] = j
        if L-next[-1] == next[-1]:
            return True
        return False

solution = Solution()
s = "abcabcabcabc"
solution.repeatedSubstringPattern(s)