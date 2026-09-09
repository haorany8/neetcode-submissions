class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int n_ = nums.size() - 1;

        while(nums.size() != 0){
            int remind = target - nums.back();
            nums.pop_back();

            auto iter_ = find(nums.begin(), nums.end(), remind);

            if (iter_ != nums.end()) {
                int idx = iter_ - nums.begin();        
                return {idx, n_};
            }
            n_ -= 1;

        }
    }
};
