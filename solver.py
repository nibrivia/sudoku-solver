from sudoku import *
from infer import infer

DEBUG = False
global_count = 0

global backtracks
backtracks = 0


def next_empty(sudoku):
    for row in sudoku.rows:
        for position, value in row:
            if value == 0:
                return position

def solve(sudoku, prefix = ""):
    global global_count
    global backtracks
    global_count += 1

    if not sudoku.is_valid():
        return False

    changes = infer(sudoku)

    if not sudoku.is_valid():
        for pos, _ in changes:
            sudoku[pos] = 0
        backtracks += 1
        return False

    if sudoku.is_full():
        return True

    # Find the next empty cell
    cell_pos = next_empty(sudoku)
    assert cell_pos is not None

    # Attempt each immediately valid option
    possible_guesses = sudoku.possibles[cell_pos]
    for cell_guess in possible_guesses:
        sudoku[cell_pos] = cell_guess

        global DEBUG
        if DEBUG:
            print(prefix + "Guessing " + str(cell_guess) + " at " + str(cell_pos))
            print(sudoku)
            print()

            user = input("Step? ")
            if user == "quit": return True # hack to exit cleanly
            if user == "continue": DEBUG=False # hack to exit cleanly


        # recurse
        if solve(sudoku):
            # We did it!
            return True

    # We only get here if we've gone through every option and failed
    backtracks += 1
    sudoku[cell_pos] = 0
    for pos, _ in changes:
        sudoku[pos] = 0
    return False

import sys

def get_filename():
    if len(sys.argv) >= 2:
        return sys.argv[1]
    else:
        return input("filename? ")

def main():
    filename = get_filename()
    sudoku = sudoku_from_file(filename)
    print("Solving:\n%s" % sudoku)

    solved = solve(sudoku)
    print("\nSolved? %s" % solved)
    print("%s" % sudoku)

    print("\nCount: %s" % global_count)
    print("Backtracks: %s" % backtracks)


if __name__ == "__main__":
    main()
