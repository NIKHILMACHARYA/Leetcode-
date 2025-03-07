class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # step 1
        grid2 = []
        for i in range(len(grid[0])):
            column = []
            for j in range(len(grid)):
                column.append(grid[j][i])
            grid2.append(column)
        
        # step 2
        counter = 0
        for row in grid:
            counter += grid2.count(row)
        
        # step 3
        return counter