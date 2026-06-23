class Solution:
    def binarySearch(self, row: List[int], target: int)->bool:
        left = 0
        right = len(row) - 1
        while left<=right :
            mid = (left+right)//2
            if row[mid] == target :
                return True
            elif target>row[mid] :
                left = mid + 1
            else:
                right = mid-1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if matrix[i][0]<=target and matrix[i][m-1]>=target:
                return self.binarySearch(matrix[i],target)
        return False
            
        