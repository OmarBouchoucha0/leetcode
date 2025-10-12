class Solution:
    # binary search to find the row 
    # then binary search to find the col
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        middle_row = len(matrix) // 2
        middle_col = len(matrix[0]) // 2
        while not matrix[0] < target < matrix[-1]:
