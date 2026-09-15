class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n=len(asteroids)
        stac = []
        for i in range(n):
            while stac and asteroids[i]<0 and stac[-1]>0:
                if stac[-1]<abs(asteroids[i]):
                   stac.pop()
                   continue
                elif stac[-1] == abs(asteroids[i]):
                    stac.pop()
                break
            else:
                stac.append(asteroids[i])
             
        return stac 
            
        
        