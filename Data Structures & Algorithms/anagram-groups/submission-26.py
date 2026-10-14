class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []
        pre_map = {}

        for i, word in enumerate(strs):
            key_ = tuple(sorted(word))
            if key_ not in pre_map:
                pre_map[key_] = [i]
            else:
                pre_map[key_].append(i)
        
        for value_ in pre_map.values():
            tmp = []
            for j in value_:
                tmp.append(strs[j])
            output.append(tmp)
        return output
