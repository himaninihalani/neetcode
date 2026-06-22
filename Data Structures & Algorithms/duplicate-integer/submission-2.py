class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      mpp = {}
      for i in range(len(nums)):
         if nums[i] in mpp:
            return True
         mpp[nums[i]] = 1

      return False