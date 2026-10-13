class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, c in enumerate(nums):
            if c == target:
                return i
            if c > target:
                return int(-1)
        return int(-1)