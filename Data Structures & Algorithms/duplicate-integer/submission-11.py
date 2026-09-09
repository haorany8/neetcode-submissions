class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            #tmp = nums[0]
            tmp = nums.pop()
            if tmp in nums:
                return True

        return False