class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        cl = len(matrix[0])

        for i in range(r):
            for j in range(i + 1, cl):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for k in range(r):
            matrix[k].reverse()
        
        return matrix
            
