class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        nbFresh,idxRotten=0,[]
        m,n=len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2: idxRotten.append((i,j))
                elif grid[i][j]==1: nbFresh+=1

        time=0

        while nbFresh>0 and len(idxRotten)>0:
            time+=1
            for _ in range(len(idxRotten)):
                i,j=idxRotten.pop(0)
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    x, y = i + dx, j + dy
                    if x < 0 or x == m or y < 0 or y == n:
                        continue
                    if grid[x][y] == 0 or grid[x][y] == 2:
                        continue
                        
                    nbFresh -= 1
                    grid[x][y] = 2
                    idxRotten.append((x, y))

        return time if nbFresh == 0 else -1
        