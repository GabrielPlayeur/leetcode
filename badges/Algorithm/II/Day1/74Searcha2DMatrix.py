class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n,m=len(matrix),len(matrix[0])
        l,r=0,m*n-1
        while l<=r:
            mid=(l+r)//2
            val=matrix[mid//m][mid%m]
            if val==target:
                return True
            elif target<val:
                r=mid-1
            else:
                l=mid+1
        return False