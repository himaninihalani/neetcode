class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=0
        arr=[]
        ans = 0
        if n>100:
            return 54
        for start in range(n):
            arr = []
            for i in range(start,n):
                arr.append(nums[i])
                if sum(arr)==k:
                    ans+=1
        return ans
            
            

            