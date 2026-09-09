class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> output;

        for (const auto&word : strs){
            vector<int> map_(26, 0);
            for (const auto&char_ : word){
                map_[char_ - 'a']++;
            }

            string key_ = to_string(map_[0]);
            for (int i = 1; i < 26; ++i){
                key_ += ',' + to_string(map_[i]);
            }


            output[key_].push_back(word);
        }

        vector<vector<string>> result;
        for (const auto& pair : output){
            result.push_back(pair.second);

        }
        return result;
    }
};
