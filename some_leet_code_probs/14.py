class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str=strs[0]
        for i in strs:
            if len(i) < len(min_str):
                min_str=i
        j=0
        while j!=len(min_str)+1:
            occ=0 
            for s in strs:
                if s[0:len(min_str)-j:]==min_str[0:len(min_str)-j:]:
                    occ+=1
                else:
                    j+=1
                    break 
            if occ==len(strs):
                return min_str[0:len(min_str)-j:]
        return ""
            
