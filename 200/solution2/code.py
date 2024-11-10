def numIslands(self, grid: List[List[str]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    res = 0

    def bfs(r: int, c: int) -> None:
        queue = deque([(r, c)])
        grid[r][c] = '0'

        while queue:
            row, col = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1':
                res += 1
                bfs(r, c)

    return res