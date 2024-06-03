class Solution:
    
    def appendCharacters(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        pointer = 0
        looking_for=0

        while(pointer < m and looking_for < n):
            if(s[pointer] == t[looking_for]):
                looking_for = looking_for + 1
            pointer += 1
        return n-looking_for