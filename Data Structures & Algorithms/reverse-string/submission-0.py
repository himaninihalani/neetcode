class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        while left<right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left = left+1
            right = right-1
        
        return s
