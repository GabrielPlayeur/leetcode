class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        initColor = image[sr][sc]
        if initColor == color: return image
        image[sr][sc]=color
        if sr-1 > -1 and image[sr-1][sc] == initColor: #check top
            image=self.floodFill(image,sr-1,sc,color)
        if sr+1<len(image) and image[sr+1][sc] == initColor: #check bottom
            image=self.floodFill(image,sr+1,sc,color)
        if sc-1>-1 and image[sr][sc-1] == initColor: #check left
            image=self.floodFill(image,sr,sc-1,color)
        if sc+1<len(image[0]) and image[sr][sc+1] == initColor: #check right
            image=self.floodFill(image,sr,sc+1,color)
        return image