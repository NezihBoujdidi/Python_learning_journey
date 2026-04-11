class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for num in nums1:
            if num in nums2 and num not in intersection:
                intersection.append(num)
        return intersection

//Faster solution

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        nums2 = set(nums2)
        for num in nums1:
            if num in nums2 and num not in intersection:
                intersection.add(num)
        intersectionArr = []
        for num in intersection:
            intersectionArr.append(num)
        return intersectionArr
