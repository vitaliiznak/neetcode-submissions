class Solution:

    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        size = rows * columns
        l = 0
        r = size - 1
        
        while  l <= r:
            m = l + (r-l)//2
            candidate = matrix[m//columns][m % columns]
            if candidate  == target:
                return True
            elif candidate < target:
                l = m + 1
            elif candidate > target:
                r = m - 1 
        return False

        
         
        