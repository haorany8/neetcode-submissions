class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        return nums[-1]