class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hash_map;
        vector<vector<int>> fre_(nums.size() + 1);

        for (int num : nums){
            hash_map[num] = 1 + hash_map[num];
        }

        for (const auto&entry : hash_map){
            fre_[entry.second].push_back(entry.first);
        }

        vector<int> res;

        for (int i = fre_.size() - 1; i > 0; --i){
            for (auto value : fre_[i]){
                res.push_back(value);
                if (res.size() == k){
                    return res;
                }

            }

        }
        return res;
    }
};
