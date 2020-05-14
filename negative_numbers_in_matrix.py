def countNegatives(grid):
    negatives = 0
    for lists in grid:
        for num in lists:
            if num <0:
                negatives += 1
    return negatives
