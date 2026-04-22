class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        grid = {}  # key = (box_row, box_col)

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                # Check row
                if val in rows[i]:
                    return False
                rows[i].add(val)

                # Check column
                if val in cols[j]:
                    return False
                cols[j].add(val)

                # Check 3x3 grid
                box = (i // 3, j // 3)
                if box not in grid:
                    grid[box] = set()

                if val in grid[box]:
                    return False
                grid[box].add(val)

        return True