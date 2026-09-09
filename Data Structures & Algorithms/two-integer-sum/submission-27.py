class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre_map = {}

        for i,value in enumerate(nums):
            left_ = target - value
            if left_ in pre_map:
                return [pre_map[left_], i]
            else:
                pre_map[value] = i