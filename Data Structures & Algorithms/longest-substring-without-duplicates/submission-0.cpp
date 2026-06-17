class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = 0;
        int max = 0;
        int n = s.size();
        string ans = "";
        unordered_map<char , int> mpp;
        int start = 0;
        for(int i=0;i<n;i++){
            if(mpp.find(s[i]) != mpp.end() && mpp[s[i]] >= start){
               start = mpp[s[i]] + 1;
               len = i-start;
               }
            mpp[s[i]] = i;
            len++;

            if(max < len){
                max = len;
            }
      }
      return max;
    }
};
