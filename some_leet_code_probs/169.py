class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurences = {}
        maj_elm_occ = 0
        maj_elm = 0
        for i in range(len(nums)):
            if nums[i] in occurences:
                occurences[nums[i]]+=1
            else:
                occurences[nums[i]] = 1
        for (k,v) in occurences.items():
            if v > maj_elm_occ:
                maj_elm_occ = v
                maj_elm = k
        return maj_elm
