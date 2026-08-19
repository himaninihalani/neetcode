class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        
        ans = []
        
        i=0
        j=0
        while i<n and j<m:
            ans.append(word1[i])
            ans.append(word2[j])
            i = i+1
            j = j+1

        if i<n:
            ans.append(word1[i:])
        if j<m:
            ans.append(word2[j:])
        return "".join(ans)