"""
Problem : 542. 01 Matrix
Difficulty: Medium
Topics   : Array, Dynamic Programming, Breadth-First Search, Matrix
Runtime  : 104
Memory   : 21292000
Language : python3
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        q = deque()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]


        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1):
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
        
        return mat

