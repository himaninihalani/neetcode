class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        if k==n:
            return arr
        left = 0
        right = n-1
        while left<right:
            mid = (left+right)// 2
            
            if arr[mid]<x:
                left = mid+1
            else:
                right = mid
        a = left-1
        b = left
        
        i = 0
        ans = []
        while i<k :

            if b>=n or (a>=0 and (abs(arr[a] - x) <= abs(arr[b] - x))):
                ans.append(arr[a])
                a-=1
            else:
                ans.append(arr[b])
                b+=1
            i+=1
        ans.sort()
        return ans
            


                    