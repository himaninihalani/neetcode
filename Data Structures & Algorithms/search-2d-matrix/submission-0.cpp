class Solution {
public:
    bool binarysearch(vector<int>& row , int target){
        int left = 0;
        int right = row.size()-1 ;
        while(left<=right){
            int mid = (left+right)/2;
            if(row[mid]==target){
                return true;
                break;
            }
            else if(target>row[mid]){
                left=mid+1;
            }
            else{
                right = mid-1;
            }
        }
        return false;
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        if(n==0) return false;
        int m = matrix[0].size();
        int j =0;
        for(int i=0;i<n;i++){
            if(matrix[i][0]<=target && target<=matrix[i][m-1]){
               return binarysearch(matrix[i],target); 
            }
        }
        return false;
    }
};
