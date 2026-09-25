class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = 0
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j+=1
        return nums