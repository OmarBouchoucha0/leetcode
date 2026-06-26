class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rows = []
        cols = []

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows.append(r)
                    cols.append(c)

        for r in range(ROWS):
            for c in range(COLS):
                if r in rows or c in cols:
                    matrix[r][c] = 0
