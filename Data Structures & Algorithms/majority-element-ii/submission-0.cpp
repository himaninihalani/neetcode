class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        std::vector<int> ans;
        int n=nums.size();
        unordered_map<int,int> mpp;
        for(int i=0;i<n;i++){
            mpp[nums[i]]++;
            if(mpp[nums[i]]==n/3+1){
                ans.push_back(nums[i]);
            }
        }
        return ans;

    }
};