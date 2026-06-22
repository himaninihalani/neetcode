class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s)-1
        for i in range (len(s)):
            
            while j > i and s[j].isalnum() == False:
                j -=1
            if s[i].isalnum() == False:
                continue
            if i >=j:
                break
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
            j -=1
        return True