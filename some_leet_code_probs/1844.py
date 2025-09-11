class Solution(object):
    def replaceDigits(self, s):
        alphabet='abcdefghijklmnopqrstuvwxyz'
        clean_s=''
        for i in range(len(s)):
            if i%2 != 0:
                clean_s += alphabet[(alphabet.index(s[i-1]))+ int(s[i]) ]
            else:
                clean_s += s[i]
        return clean_s
