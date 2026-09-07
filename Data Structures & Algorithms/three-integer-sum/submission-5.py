class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        
        for i in range(0,n-1):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if total==0:
                    temp =  [nums[i],nums[left],nums[right]]
                    res.add(tuple(temp))
                    left += 1
                    right -= 1
                    
                elif total<0:
                    left+=1
                elif total>0:
                    right-=1
        return [list(i) for i in res] 