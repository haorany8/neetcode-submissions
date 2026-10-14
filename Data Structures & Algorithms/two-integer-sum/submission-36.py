class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dir_ = defaultdict(int)

        for i, n in enumerate(nums):
            left = target - n
            if n in dir_:
                return [dir_[n], i]
            else:
                dir_[left] = i
