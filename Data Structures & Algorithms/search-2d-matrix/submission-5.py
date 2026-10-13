class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)

        i = 0

        while i < rows and matrix[i][0] <= target:
            if matrix[i][0] == target:
                return True

            i += 1

        if i == rows:
            for j in range(len(matrix[i - 1])):
                if matrix[i - 1][j] == target:
                    return True
        else:
            for j in range(len(matrix[i - 1])):
                if matrix[i - 1][j] == target:
                    return True
        

        return False

             