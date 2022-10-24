grid = [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]

m = len(grid)
n = len(grid[0])

ans = list(range(n))

for i in range(m):
    for j in range(n):
        column = ans[j]
        if column == -1:
            continue
        next_column = column + grid[i][column]
        if next_column < 0 or next_column >= n or grid[i][next_column] == -grid[i][column]:
            ans[j] = -1
            continue
        ans[j] += grid[i][column]
        print(ans)

print(ans)
