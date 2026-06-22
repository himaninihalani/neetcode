class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        for i in range(n):
            for j in range(n):
                if(i==j):
                    continue
                else:
                    ans[i]=ans[i]*nums[j]
        return ans
        
        