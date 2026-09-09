class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pre_map = defaultdict(int)
        output = []
        for i, value in enumerate(nums):
            pre_map[value] += 1
        
        sorted_map = sorted(pre_map, key=pre_map.get, reverse = True)

        for i in range(k):
            output.append(sorted_map[i])
        
        return output