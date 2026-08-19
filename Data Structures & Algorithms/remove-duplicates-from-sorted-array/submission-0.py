class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash_map = {}
        j = 0
        for i in range(0,len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
                nums[j] = nums[i]
                j = j+1
        return j
                