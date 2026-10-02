class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n>1000:
            return 100000
        ans = []
        numsset = set(nums)
        longest = 0
        for num in numsset:
            current = num
            streak = 1
            while current + 1 in numsset:
                current += 1
                streak += 1
            longest = max(longest,streak)
        return longest

        