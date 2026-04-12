class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = []
        num2_dict = {}
        for num in nums2:
            if num in num2_dict:
                num2_dict[num]+=1
            else:
                num2_dict[num]=1
        for num in nums1:
            if num in num2_dict:
                if num2_dict[num] == 0:
                    del num2_dict[num]
                else:
                    seen.append(num)
                    num2_dict[num]-=1
        return seen
