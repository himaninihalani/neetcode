class Solution {
public:
    int arrangeCoins(int n) {
        if(n == 0) return 0;
        int cnt = 1;
        while(cnt<=n){
              n = n-cnt;
              cnt++;
        }
        return cnt-1;
    }
};