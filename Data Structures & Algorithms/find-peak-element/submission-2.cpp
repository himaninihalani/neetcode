class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        int left = 0 ; 
        int right = n - 1;
        while(left<right){
            int mid=(right+left)/2;
           
            if(nums[mid+1]>nums[mid]){
                left = mid+1;
            }
            else{
                right = mid;
            }
        }
        return left;
    }
};