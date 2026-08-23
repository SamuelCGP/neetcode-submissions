#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<int, int> frequency_s, frequency_t;

        for(int i = 0; i < s.length(); i++){
            frequency_s[s[i]]++;
        }
        for(int i = 0; i < t.length(); i++){
            frequency_t[t[i]]++;
        }

        for(int i = 0; i < s.length(); i++){
            if (frequency_s[s[i]] != frequency_t[s[i]]) {
                return false;
            }
        }

        return true;
    }
};
