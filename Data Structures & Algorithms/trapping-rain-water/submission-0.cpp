class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int sum = 0;
        int  trapped = 0;
        for(int i=0;i<n;i++){
        int left_max = 0;
        int right_max=0;

            for(int j=0;j<i;j++){
                if(height[j]>left_max){
                    left_max=height[j];
                }
            }
            for(int k=i;k<n;k++){
                if(height[k]>right_max){
                    right_max=height[k];
                }
            }
            trapped=min(left_max,right_max)-height[i];
            if(trapped>0){
               sum = sum+trapped;
            }
        }
        return sum;
    }
};
