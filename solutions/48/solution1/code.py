class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)

        for r in range(N):
            for c in range(r, N):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in matrix:
            r.reverse()