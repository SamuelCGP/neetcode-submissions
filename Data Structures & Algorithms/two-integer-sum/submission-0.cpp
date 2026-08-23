class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int wanted_num = target - nums[i];
            if (seen.count(wanted_num)) {
                return {seen[wanted_num], i};
            }
            seen[nums[i]] = i;
        }

        return {};
    }
};
