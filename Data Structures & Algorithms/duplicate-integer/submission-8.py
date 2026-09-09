class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):

            tmp = nums[0]
            nums.pop(0)
            if tmp in nums:
                return True

        return False