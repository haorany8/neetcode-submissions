class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        vector<int> hash_map(26, 0);

        for (int i = 0; i < s.length(); i++){
            hash_map[s[i] - 'a']++;
            hash_map[t[i] - 'a']--;
        }
        
        for (int val : hash_map){
            if (val != 0){
                return false;
            }
        }
        return true;

    }
};
