class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        best = 1
        length = 1
        pre = sorted_nums[0]
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - pre == 0:
                continue
            elif sorted_nums[i] - pre == 1:
                length += 1
                best = max(length, best)
            else:

                length = 1

            pre = sorted_nums[i]


        return best