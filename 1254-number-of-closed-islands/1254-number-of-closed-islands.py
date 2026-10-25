class Solution:
    def closedIsland(self, grid):
        R, C = len(grid), len(grid[0])
        tag = [row[:] for row in grid]

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    if r == 0 or c == 0 or r == R - 1 or c == C - 1:
                        tag[r][c] = -1
                    else:
                        tag[r][c] = r * C + c

        changed = True
        while changed:
            changed = False
            for r in range(R):
                for c in range(C):
                    if grid[r][c] == 0:
                        best = tag[r][c]
                        if r > 0 and grid[r - 1][c] == 0:
                            best = min(best, tag[r - 1][c])
                        if r < R - 1 and grid[r + 1][c] == 0:
                            best = min(best, tag[r + 1][c])
                        if c > 0 and grid[r][c - 1] == 0:
                            best = min(best, tag[r][c - 1])
                        if c < C - 1 and grid[r][c + 1] == 0:
                            best = min(best, tag[r][c + 1])
                        if best != tag[r][c]:
                            tag[r][c] = best
                            changed = True

        closed = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0 and tag[r][c] != -1:
                    closed.add(tag[r][c])
        return len(closed)