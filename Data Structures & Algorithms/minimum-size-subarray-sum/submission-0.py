class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        sumosa = nums[left]
        minimu_length = float('inf')
        window = 1
        while left<n:  
            if sumosa>=target:
                minimu_length = min(minimu_length , window)
                sumosa -= nums[left]
                left += 1
                window-=1
            else:
                right += 1
                if right<n:
                    sumosa += nums[right]
                    window += 1  
                else:
                    break
                
                
        return minimu_length if minimu_length!=float('inf') else 0

