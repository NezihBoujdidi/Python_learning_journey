class Solution:
    def reverseString(self, s: List[str]) -> None:
        reversed_string=''.join(s)[::-1]
        for i in range(len(reversed_string)):
            s[i]=reversed_string[i]
        print(s)
        
