class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)

        return res