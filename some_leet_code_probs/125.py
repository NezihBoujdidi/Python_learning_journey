class Solution(object):
    def isPalindrome(self, s):
        alphanum ='abcdefghijklmnopqrstuvwxyz01234567894'
        clean_s = ''
        for char in s:
            if char.lower() not in alphanum:
                pass
            else:
                clean_s += char.lower()
        reversed_s = clean_s[::-1]
        return clean_s == reversed_s             
                 
        
        
