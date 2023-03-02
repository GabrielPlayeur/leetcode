class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if (r*c)!=(len(mat)*len(mat[0])): return mat
        res = [[0]*c for _ in range(r)];
        m=len(mat[0])
        for i in range(r*c):
            res[i//c][i%c] = mat[i//m][i%m]
        return res