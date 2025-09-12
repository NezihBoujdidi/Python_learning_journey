import re
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_string = ','.join(str(numb) for numb in nums)
        handled=''
        for numb in nums:
            if len(re.findall(fr'{str(numb)}',nums_string))%2 == 0 and handled.find(str(numb))==-1:
                handled+= str(numb)+','
            elif handled.find(str(numb))!=-1:
                continue
            elif len(re.findall(fr'{str(numb)}',nums_string))%2 != 0:
                return False
        return True    
