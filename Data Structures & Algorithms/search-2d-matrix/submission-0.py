class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = (rows * cols) - 1
        while l <= r:
            m = l + (r - l) // 2
            m_val = matrix[m // cols][m % cols]
            if m_val == target:
                return True
            elif m_val < target:
                l = m + 1
            else:
                r = m - 1
        return False