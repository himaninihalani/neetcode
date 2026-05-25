class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
       unordered_map<int, int> Map;
       for(int num:nums){
        if(Map.find(num)!=Map.end()){
           return true;
        }
        Map[num]++;
       }
       return false; 
    }
};