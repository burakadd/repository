s = [[7, 8, 4, 1, 5, 9, 3, 2, 6],
     [5, 3, 9, 6, 7, 2, 8, 4, 1],
     [6, 1, 2, 4, 3, 8, 7, 5, 9],
     [9, 2, 8, 7, 1, 5, 4, 6, 3],
     [3, 5, 7, 8, 4, 6, 1, 9, 2],
     [4, 6, 1, 9, 2, 3, 5, 8, 7],
     [8, 7, 6, 3, 9, 4, 2, 1, 5],
     [2, 4, 3, 5, 6, 1, 9, 7, 8],
     [1, 9, 5, 2, 8, 7, 6, 3, 4]]
for i in s:
    print(i)


def sudoku(matrix):
    def rowchecker(matrix):
        return all(sorted(row) == list(range(1, len(matrix) + 1)) for row in matrix)

    def transponirovanie(matrix):
        return [[row[columnnumber] for row in matrix] for columnnumber in range(len(matrix))]

    def kvadrirovanie(matrix):
        squares = []
        step = int(len(matrix) ** 0.5)
        for rownumber in range(0, len(matrix), step):
            for columnnumber in range(0, len(matrix), step):
                squares.append([matrix[row][column] for row in range(
                    rownumber, rownumber + step) for column in range(columnnumber, columnnumber + step)])
        return squares
    return all((rowchecker(matrix), rowchecker(transponirovanie(matrix)), rowchecker(kvadrirovanie(matrix))))



print(sudoku(s))
def isquare(row, column, matrix):
   0 <= row





def sudokusolver(matrix):
    for row in matrix:
        for i in row:
