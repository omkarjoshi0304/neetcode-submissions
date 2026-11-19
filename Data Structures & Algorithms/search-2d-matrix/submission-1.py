class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows = len(matrix)
        Col = len(matrix[0])

        left = 0
        right = (Rows * Col) - 1

        while left <= right:

            mid = (left + right) // 2

            rows = mid // Col
            col = mid % Col

            mid_val = matrix[rows][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False