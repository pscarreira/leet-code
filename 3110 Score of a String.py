class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        pos = 1

        while pos < len(s):
            score += abs(ord(s[pos]) - ord(s[pos-1]))
            pos+=1

        return score