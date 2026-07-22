class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    dup = True
        return dup