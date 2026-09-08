class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        
        while left<right:
            while left<right and s[left].isalnum() == False:
                left = left+1   
            while left<right and s[right].isalnum() == False:
                right = right-1
            if s[left].lower() != s[right].lower():
                skip_left = s[left + 1 : right + 1]
                skip_right = s[left : right]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
                  
            left = left + 1
            right = right - 1
            
        return True
        