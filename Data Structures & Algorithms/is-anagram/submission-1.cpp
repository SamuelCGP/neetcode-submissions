#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> frequency;

        for(int i = 0; i < s.length(); i++){
            frequency[s[i]]++;
        }
        for(int i = 0; i < t.length(); i++){
            frequency[t[i]]--;
            if (frequency[t[i]] < 0) {
                return false;
            }
        }

        for (const auto& [key, value] : frequency) {
            if (value != 0) {
                return false;
            }
        }

        return true;
    }
};
