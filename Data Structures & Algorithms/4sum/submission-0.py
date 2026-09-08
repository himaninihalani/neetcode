class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                left = j+1
                right = n-1
                while left < right:
                    total = nums[i]+nums[j]+nums[left]+nums[right]
                    if total == target:
                        temp =  [nums[i],nums[left],nums[right],nums[j]]
                        res.add(tuple(temp))
                        left += 1
                        right -= 1
                    elif total<target:
                        left+=1
                    elif total>target:
                        right-=1
        return [list(i) for i in res]

                        

        
        