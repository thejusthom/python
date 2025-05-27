class Solution(object):
    def searchMatrix(self, matrix, target):
        COL,ROW = len(matrix[0]), len(matrix)
        top,bottom = 0,ROW-1
        while top <= bottom:
            row =  (top + bottom) //2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        if not (top <= bottom):
            return False
        
        row =  (top + bottom) // 2
        l,r = 0, COL-1
        while l < r:
            m = (l+r)//2
            if matrix[row][m] == target:
                return True                
            elif matrix[row][m] < target:
                l = m+1
            else:
                r = m-1
        return False

t = 4
ma = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(Solution().searchMatrix(ma,t))