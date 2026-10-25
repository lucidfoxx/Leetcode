class Solution:
    def closedIsland(self, grid):
        R, C = len(grid), len(grid[0])
        g = [row[:] for row in grid]

        for r in range(R):
            for c in range(C):
                if g[r][c] == 0 and (r == 0 or c == 0 or r == R - 1 or c == C - 1):
                    g[r][c] = 2

        changed = True
        while changed:
            changed = False
            for r in range(R):
                for c in range(C):
                    if g[r][c] == 0:
                        if (r > 0 and g[r - 1][c] == 2) or (r < R - 1 and g[r + 1][c] == 2) or (c > 0 and g[r][c - 1] == 2) or (c < C - 1 and g[r][c + 1] == 2):
                            g[r][c] = 2
                            changed = True

        count = 0
        for r in range(R):
            for c in range(C):
                if g[r][c] == 0:
                    count += 1
                    g[r][c] = 3
                    changed = True
                    while changed:
                        changed = False
                        for i in range(R):
                            for j in range(C):
                                if g[i][j] == 0:
                                    if (i > 0 and g[i - 1][j] == 3) or (i < R - 1 and g[i + 1][j] == 3) or (j > 0 and g[i][j - 1] == 3) or (j < C - 1 and g[i][j + 1] == 3):
                                        g[i][j] = 3
                                        changed = True
        return count