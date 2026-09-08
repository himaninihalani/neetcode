class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        
        target=1
        for num in nums:
            if num==target:
                target+=1
            
            elif num>target:
                return target
        return target
        
        

            

        