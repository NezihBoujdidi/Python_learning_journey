class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        digits[i] = (digits[i]+1) % 10 
        while (digits[i] == 0):
            if (i!=0):
                digits[i-1] = (digits[i-1]+1) % 10
                i-=1
            if (i==0 and digits[i] == 0):
                digits.append(0)
                for j in range(len(digits)-1,1,-1):
                    digits[j] = digits[j-1]
                digits[0] = 1
        return digits
