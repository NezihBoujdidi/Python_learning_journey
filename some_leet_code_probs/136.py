class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occurences = {}
        for i in range(len(nums)):
            if nums[i] in occurences:
                occurences[nums[i]]+=1
            else:
                occurences[nums[i]] = 1
        for k,v in occurences.items():
            if (v ==1):
                return k
        
            
