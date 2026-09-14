class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n_ = len(nums)
        res = []

        while len(nums) >= 3:
            target = -nums[0]
            nums.pop(0)

            l, r = 0, len(nums) - 1

            while l < r:
                while nums[l] + nums[r] > target and l < r:
                    r = r - 1
                while nums[l] + nums[r] < target and l < r:
                    l = l + 1
                if nums[l] + nums[r] == target and l < r :
                    if sorted([-target, nums[l], nums[r]]) not in res:
                        res.append(sorted([-target, nums[l], nums[r]]))
                    l = l + 1
                    r = r - 1
        return res