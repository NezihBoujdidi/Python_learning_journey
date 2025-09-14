class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 1
        current = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != current:
                current = nums[i]
                nums[unique] = nums[i]
                unique += 1

        print(f'{unique}, nums = {nums}')
        return unique
