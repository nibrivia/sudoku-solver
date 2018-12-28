def infer(sudoku):
    fn_list = [only_one]
    changes = []
    for fn in fn_list:
        new_changes = fn(sudoku)
        changes.extend(new_changes)
        if len(new_changes) > 0:
            changes.extend(infer(sudoku))

    return changes

def group_to_set(group):
    indices, values = zip(*group)
    v =  set(v for v in values if v != 0)
    return v

OPTIONS = set(range(1,10))

def group_empty_cells(group):
    return [pos for pos, val in group if val == 0]

def only_one(sudoku):
    changes = []
    for row in sudoku.rows:
        empty_cells = group_empty_cells(row)
        for pos in empty_cells:
            possibles = sudoku.possibles[pos]
            if len(possibles) == 1:
                new_val = list(possibles)[0]
                sudoku[pos] = new_val
                changes.append((pos, new_val))

    return changes
