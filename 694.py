def numDistinctIslands(self, grid: List[List[int]]) -> int:
    def dfs(start, shape, i, j):
        if  0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            # track shape using starting coords
            shape.append((i-start[0], j-start[1]))
            grid[i][j] = 2  # make sure we don't visit again
            dfs(start, shape, i+1, j)
            dfs(start, shape, i-1, j)
            dfs(start, shape, i, j+1)
            dfs(start, shape, i, j-1)
        return shape

    unique_islands, ans = set(), 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # shape of island we just visited
                island = tuple(dfs((i, j), [], i, j))
                if island not in unique_islands:
                    unique_islands.add(island)
                    ans += 1
    return ans
