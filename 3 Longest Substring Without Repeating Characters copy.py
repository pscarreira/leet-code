class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lswr = ''
        partial_lswr=''

        for pointer in s:
            if(pointer in partial_lswr):
                if(len(lswr) < len(partial_lswr)):
                    lswr = partial_lswr
                
                new_start = partial_lswr.index(pointer) + 1
                partial_lswr = partial_lswr[new_start:]
                partial_lswr = partial_lswr + pointer
            else:
                partial_lswr = partial_lswr + pointer

        if(len(lswr) < len(partial_lswr)):
            lswr = partial_lswr

        return len(lswr)
