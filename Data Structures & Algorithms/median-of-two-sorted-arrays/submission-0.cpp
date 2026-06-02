class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        vector<int> nums3;

        for(int i=0;i<n;i++){
            nums3.push_back(nums1[i]);
        }
        for(int j=0;j<m;j++){
           nums3.push_back(nums2[j]);
        }

        sort(nums3.begin(),nums3.end());
        int mid = (m+n)/2;
        if((m+n)%2 != 0){
           return nums3[mid];
        }
        else{
            return (nums3[mid]+nums3[mid-1])/2.0;
        }
    }
};
