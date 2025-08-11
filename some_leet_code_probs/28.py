class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(haystack)<len(needle)):
            return -1
        j=0
        while j!=(len(haystack)-len(needle))+1:
            if haystack[j:len(needle)+j:]==needle:
                return j
            else:
                j+=1
        return -1
