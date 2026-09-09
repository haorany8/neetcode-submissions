class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        fre_ = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)
        
        for value, count in hash_map.items():
            fre_[count].append(value)
        
        res = []

        for i in range(len(fre_) - 1, 0 , -1):
            for num in fre_[i]:
                res.append(num)
            if len(res) == k:
                return res