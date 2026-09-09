class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) -1
        while nums:
            remind = target - nums[-1]
            nums.pop()
            if remind in nums:
                idx = nums.index(remind)
                return [idx, n]
            
            n -= 1
        
