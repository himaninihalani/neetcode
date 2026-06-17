class Solution {
public:
    bool isAnagram(string s, string t) {
      int n = s.size();
      int m = t.size();
      if(m!=n){
        return false;
      }
      vector<int> arr(26,0);
      for(int i=0;i<n;i++){
        arr[s[i] - 'a']++;
      }
      for(int j=0;j<m;j++){
        arr[t[j] - 'a']--;
      }
      for(int k=0;k<arr.size();k++){
        if(arr[k]!=0){
          return false;
        }
      }
      return true;
    }
};
