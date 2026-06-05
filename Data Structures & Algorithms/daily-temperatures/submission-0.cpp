class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> ans;
        for(int i=0;i<n;i++){
            bool found = false;
            for(int j=i;j<n;j++){
                if(temperatures[i]<temperatures[j]){
                    ans.push_back(j-i);
                    found = true;;
                    break;
                }
                }
                if(found == false){
                    ans.push_back(0);
                }
            }
        
        return ans;
    }
};
