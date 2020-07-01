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

    #recurrentsive dfs
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
            resultult = set()
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == target:
                        resultult.add((x,y))
            return resultult


        rotten = createSet(grid,2)
        fresulth = createSet(grid,1)

        time = 0
        while len(fresulth) > 0:
            turned_rot = set()
            for x,y in fresulth:
                #check all sides for rotten neihbors
                if (x+1,y) in rotten or (x-1,y) in rotten or (x,y+1) in rotten or (x,y-1) in rotten:
                    turned_rot.add((x,y))
            # print(time, rotten, fresulth, turned_rot)
            if len(turned_rot) == 0:
                return -1
            fresulth.difference_update(turned_rot)
            rotten.update(turned_rot)
            time += 1

        return time


oranges = Orange_Solution()
print(oranges.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

class Schedule_Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0]*numCourses
        graph = {}

        for relation in prerequisites:
            a,b = relation[0],relation[1]
            indegrees[a] += 1

            node_list = []
            if b not in graph:
                node_list.append(a)
                graph[b] = node_list
            else:
                node_list = graph[b]
                node_list.append(a)
                graph[b] = node_list

        queue = []

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        result = []

        while len(queue)>0:
            currentrent = queue.pop(0)
            result.append(current)

            if current in graph:
                neighbors = graph[current]
                for neighbor in neighbors:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)

        if len(result) == numCourses:
            return result

        return []

schedule = Schedule_Solution()

print(schedule.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
