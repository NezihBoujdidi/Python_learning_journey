class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max = 0
        current = 0
        i= 0
        while i<(len(nums)-1):
            if nums[i+1]>nums[i]:
                current+=1
                i+=1
            else:
                if (max <= (current+1)):
                    max = current+1
                current = 0
                i+=1
        if (current + 1) >= max:
            return current + 1
        else:
            return max

        
