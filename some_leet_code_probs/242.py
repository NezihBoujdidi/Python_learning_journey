import re

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = True
        for i in range(len(s)):
            if len(re.findall(s[i],s)) != len(re.findall(s[i],t)):
                res = False
                break
        return res and len(s)==len(t)          
