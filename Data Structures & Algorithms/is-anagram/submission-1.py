class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        count = [0] * 26

        for i in range(n):
          count[ord(s[i])-ord('a')] += 1
        
        for j in range(m):
          count[ord(t[j])-ord('a')] -= 1
        
        for k in range(len(count)):
          if count[k] != 0:
            return  False
        
        return True