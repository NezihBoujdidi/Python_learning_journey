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

#or 2nd sol
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = strs[0]
        for string in strs:
            if len(string) < len(shortest_str):
                shortest_str = string
        for i in range(len(shortest_str),0,-1):
            all_match = True
            for string in strs:
                if string[0:i:] == shortest_str[0:i:]:
                    continue
                else:
                    all_match = False
                    break
            if all_match == True :
                return shortest_str[0:i:]
        return ""           
