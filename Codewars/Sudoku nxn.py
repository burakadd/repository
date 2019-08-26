class Sudoku(object):
    def __init__(self, data):
        self.field = data

    def is_valid(self):
        print(self.field)

        def are_rows_valid(matrix):
            return all(sorted(row) == list(range(1, len(matrix) + 1)) for row in matrix)

        def transposition(matrix):
            return [[row[column_number] for row in matrix] for column_number in range(len(matrix))]

        def block_to_row(matrix):
            rows = []
            step = int(len(matrix) ** 0.5)
            for row_number in range(0, len(matrix), step):
                for column_number in range(0, len(matrix), step):
                    rows.append([matrix[row][column] for row in range(
                        row_number, row_number + step) for column in range(
                        column_number, column_number + step)])
            return rows

        if any((isinstance(element, bool)) for row in self.field for element in row) or any(len(self.field) != len(array) for array in self.field):
            return False
        else:
            return all((are_rows_valid(self.field), are_rows_valid(
                transposition(self.field)), are_rows_valid(block_to_row(self.field))))
