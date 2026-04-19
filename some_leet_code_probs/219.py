class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if i+k+1 > len(nums):
                portion = nums[i+1:len(nums)]
            else:
                portion = nums[i+1:i+k+1]
            if nums[i] in portion:
                return True
        return False
