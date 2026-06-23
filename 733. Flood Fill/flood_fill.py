"""
Problem : 733. Flood Fill
Difficulty: Easy
Topics   : Array, Depth-First Search, Breadth-First Search, Matrix
Runtime  : 0
Memory   : 19552000
Language : python3
"""

class Solution:

    def dfs(self, image, sr, sc, color, start):
        if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1 or image[sr][sc] == color or image[sr][sc] != start:
            return
        image[sr][sc] = color
        self.dfs(image, sr + 1, sc, color, start)
        self.dfs(image, sr - 1, sc, color, start)
        self.dfs(image, sr, sc + 1, color, start)
        self.dfs(image, sr, sc - 1, color, start)


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        self.dfs(image, sr, sc, color, start)
        return image
