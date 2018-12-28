from sudoku import *

DEBUG = False
global_count = 0


def infer(sudoku):
    pass

def next_empty(sudoku):
    for row in sudoku.rows:
        for position, value in row:
            if value == 0:
                return position

def solve(sudoku, prefix = ""):
    global global_count
    global_count += 1

    if not sudoku.is_valid():
        return False

    changes = infer(sudoku)

    if sudoku.is_full():
        return True

    # Find the next empty cell
    cell_pos = next_empty(sudoku)
    assert cell_pos is not None

    # Attempt each of 1-9 in that cell
    for cell_guess in range(1, 10):
        if DEBUG:
            print(prefix + "Guessing " + str(cell_guess) + " at " + str(cell_pos))
            print(sudoku)
            print()

            user = input("Step? ")
            if user == "quit": return True # hack to exit cleanly


        sudoku[cell_pos] = cell_guess

        # Try next if not valid
        if not sudoku.is_valid():


        # The guess is valid for now, recurse

            # We did it!
            return True

    # We only get here if we've gone through every option and failed
    sudoku[cell_pos] = 0

import sys

def get_filename():
    if len(sys.argv) >= 2:
        return sys.argv[1]
    else:
        return input("filename? ")

def main():
    filename = get_filename()
    sudoku = sudoku_from_file(filename)
    print(sudoku)

    solved = solve(sudoku)
    print(solved)
    print(sudoku)
    print(global_count)


if __name__ == "__main__":
    main()
