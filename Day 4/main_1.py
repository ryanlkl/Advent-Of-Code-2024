directions = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]

grid = []

while True:
    line = [*input()]
    if not line:
        break
    grid.append(line)

rows = len(grid)
cols = len(grid[0])

count = 0
xmas = "XMAS"

for i in range(rows):
    for j in range(cols):
        if grid[i][j] != "X":
            continue

        for dx,dy in directions:
            row = i + dx
            col = j + dy
            if row < 0 or row > rows - 1 or col < 0 or col > cols - 1:
                continue

            index = 1
            while grid[row][col] == xmas[index]:
                if index == 3 and grid[row][col] == "S":
                    count += 1
                    break

                if grid[row][col] == xmas[index]:
                    row += dx
                    col += dy
                    index += 1
                else:
                    break

                if row < 0 or row > rows - 1 or col < 0 or col > cols - 1:
                    break

print(count)