class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i=0
        while i<len(nums):
            a = nums[i]
            b= nums[i]
            i+=1
            while i<len(nums) and (b+1) == nums[i] :
                b= nums[i]
                i+=1
            if a == b:
                result.append(str(a))
            else:
                result.append(str(a) + '->' + str(b))
        return result
