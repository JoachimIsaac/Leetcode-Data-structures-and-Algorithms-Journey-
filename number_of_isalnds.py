"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000

Output: 1



Example 2:
Input:
11000
11000
00100
00011

Output: 3
"""



class Solution:
    def numIslands(self, grid):
        # Recursive Depth first search
        def sinkIslands(grid, r, c):
            if grid[r][c] == "1":
                grid[r][c] = 0
            else:
                return

            if r + 1 < len(grid):  # up
                sinkIslands(grid, r + 1, c)

            if r - 1 >= 0:  # down
                sinkIslands(grid, r - 1, c)

            if c - 1 >= 0:  # left
                sinkIslands(grid, r, c - 1)

            if c + 1 < len(grid[0]):  # right
                sinkIslands(grid, r, c + 1)

        counter = 0

        # Iterate over all entries and sink the island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    counter += 1
                    sinkIslands(grid, i, j)
        return counter


grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid2 = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]

s = Solution()
print("Number of islands in grid number 2",s.numIslands(grid2))


