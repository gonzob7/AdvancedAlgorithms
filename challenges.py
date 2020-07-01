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
print(islands.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

class Orange_Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def createSet(grid, target):
            result = set()
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == target:
                        result.add((x,y))
            return result
        rotten = createSet(grid,2)
        fresh = createSet(grid,1)

        time = 0
        while len(fresh) > 0:
            turned = set()
            for x,y in fresh:
                #check all sides for rotten neihbors
                if (x+1,y) in rotten or (x-1,y) in rotten or (x,y+1) in rotten or (x,y-1) in rotten:
                    turned.add((x,y))
            # print(time, rotten, fresh, turned)
            if len(turned) == 0:
                return -1
            fresh.difference_update(turned)
            rotten.update(turned)
            time += 1

        return time

oranges = Orange_Solution()
print(oranges.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
