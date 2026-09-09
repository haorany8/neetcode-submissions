class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n_ = nums.size();
        unordered_map<int, int> pre_map;
        for (int i = 0; i < n_; i++){
            int left_ = target - nums[i];
            if (pre_map.find(left_) != pre_map.end()){
                return {pre_map[left_], i};
            }

            pre_map.insert({nums[i], i});

        }
        return {};
    }
};
