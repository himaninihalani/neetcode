class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int profit = 0;
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if((prices[j]-prices[i])>profit && i!=j){
                    profit = (prices[j]-prices[i]);
                }
            }
        }
        return profit;
    }
};
