** in a dict you can use dict.get(key,"unknown") it will return unknown if key doesn't exist **

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars={}
        for i in range(len(s)):
            if chars.get(s[i],"not in")!="not in" :
                chars[s[i]]+=1
            else:
                chars[s[i]]=1
        for k in chars:
            if chars[k]==1:
                return s.index(k)
        return -1
