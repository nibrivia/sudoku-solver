
def sudoku_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()

    assert len(lines) == 9, "Expected 9 lines"
    return Sudoku(sudoku = [[int(cell) for cell in l.split()] for l in lines])

def has_duplicates(group):
    group_no_empty = [cell for cell in group if cell != 0]
    value_set = set()
    for value in group_no_empty:
        if value in value_set:
            return True
        else:
            value_set.add(value)
    return False


class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def is_full(self):
        for row in self.sudoku:
            for cell in row:
                if cell == 0:
                    return False
        return True

    @property
    def groups(self):
        yield from self.rows
        yield from self.cols
        yield from self.squares

    @property
    def rows(self):
        for row_i, row in enumerate(self.sudoku):
            yield [ ((row_i, col_i), val) for col_i, val in enumerate(row)]

    @property
    def cols(self):
        for col_i in range(9):
            yield [row[col_i] for row in self.rows]

    @property
    def squares(self):
        sudoku = self.sudoku
        for s_i in range(3):
            for s_j in range(3):
                row_i = 3*s_i
                col_i = 3*s_j

                square = []
                for dr in range(3):
                    for dc in range(3):
                        position = (row_i+dr, col_i+dc)
                        square.append( (position, self[position]) )

                yield square

    def is_valid(self):
        for group in self.groups:
            indices, values = zip(*group)
            if has_duplicates(values):
                return False

        return True

    def __getitem__(self, position):
        r, c = position
        return self.sudoku[r][c]

    def __setitem__(self, position, value):
        r, c = position
        self.sudoku[r][c] = value

    def __str__(self):
        sudoku_str = ""

        for row in self.rows:
            for (row_i, col_i), cell in row:
                sudoku_str += str(cell) if cell != 0 else "_"
                sudoku_str += " "

                if col_i == 2 or col_i == 5:
                    sudoku_str += " "

            if row_i == 2 or row_i == 5:
                sudoku_str += "\n"
            if row_i < 8:
                sudoku_str += "\n"

        return sudoku_str

def test():
    sudoku = sudoku_from_file("hardest.txt")
    assert sudoku.is_valid(), "hardest.txt should be valid"

    bad_files = ["wrong-col.txt", "wrong-row.txt", "wrong-square.txt"]
    for filename in bad_files:
        bad_sudoku = sudoku_from_file(filename)
        assert (not bad_sudoku.is_valid()), filename + " should be not be valid"
        assert (not bad_sudoku.is_full()), filename + " should be not be full"

    full = sudoku_from_file("full.txt")
    assert full.is_valid(), "full.txt should be valid"
    assert full.is_full(),  "full.txt should be full"

    print("ok")


def main():
    sudoku = sudoku_from_file("hardest.txt")
    print(sudoku)
    print("Valid: %s" % sudoku.is_valid())
    print("Full:  %s" % sudoku.is_full())

if __name__ == "__main__":
    print("--- Test ---")
    test()

    print("\n--- Main ---")
    main()

