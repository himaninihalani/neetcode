class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n=len(s)
        m=len(g)
        g.sort()
        s.sort()
        ans = 0
        temp=[0]* n
        for i in range(m):
            for j in range(n):
                if s[j] >= g[i] and temp[j]==0:
                    ans += 1
                    temp[j]=1
                    break
        return ans 
        