class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans;
        unordered_map<int , int> mpp;
        for(int i=0;i<n;i++){
            mpp[nums[i]]++;
        }
        while(k--){
        int max_freq = 0;
        int max = 0;
        for(int j=0;j<n;j++){
            if(mpp[nums[j]]>max_freq){
                max_freq = mpp[nums[j]];
                max = nums[j];
            }
        }
        ans.push_back(max);
        mpp[max] = 0;
        }

        return ans;
    }
};
