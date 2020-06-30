from typing import List

class Island_Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        island_count = 0

        #loop through every value in grid and perform dfs
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    #make grid
                    island_count += 1

        return island_count

    #recursive dfs
    def dfs(self, grid, i, j):
        if grid[i][j] != '1':
            return

        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

islands = Island_Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
////
