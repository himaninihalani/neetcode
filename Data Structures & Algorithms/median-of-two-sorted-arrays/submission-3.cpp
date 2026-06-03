class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        
        int ite = 0;

        int mid1 = 0;
        int mid2 = 0;

        int i = 0;
        int j = 0;

        while(ite<=((m+n)/2)){
            mid2 = mid1;
           if(i<n && (j>=m || nums1[i]<nums2[j])){
            
            mid1 = nums1[i];
            i++;
            ite++;
           }
           else{
           
            mid1 = nums2[j];
            j++;
            ite++;
           }
        }

        if((m+n)%2 != 0){
            return mid1;
        }
        else{
             return (mid1+mid2)/2.0;
        }
        return -1;
    }
};
