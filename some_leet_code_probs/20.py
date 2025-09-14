class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0 or len(s)==0:
            return False
        openers = []
        for i in range(len(s)):
            if s[i] in ["(","[","{"]:
                openers.append(s[i])
            elif openers!=[] and ((s[i]==')' and openers.pop()=='(') or (s[i]==']' and openers.pop()=='[') or (s[i]=='}' and openers.pop()=='{')):
                continue
            else:
                return False
        if openers!=[]:
            return False
        else:   
            return True
