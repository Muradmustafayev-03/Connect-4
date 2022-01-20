ROWS, COLUMNS = range(1, 7), range(1, 8)


def count_horizontal(coordinates, grid):
    """
    Counts horizontal alignments for the given point in right direction
    :param coordinates: the coordinates of the cell in the grid
    :param grid: the list representing the board(grid) which is being played on
    :return: the number of cells with the same discs aligned to the right
    """
    aligned = 1
    column, row = coordinates

    if grid[row][column] == grid[row][column + 1]:
        aligned += count_horizontal([column + 1, row], grid)

    return aligned


def count_vertical(coordinates, grid):
    """
    Counts vertical alignments for the given point in up direction
    :param coordinates: the coordinates of the cell in the grid
    :param grid: the list representing the board(grid) which is being played on
    :return: the number of cells with the same discs aligned to the up
    """
    aligned = 1
    column, row = coordinates

    if grid[row][column] == grid[row + 1][column]:  # checking the next cell
        aligned += count_vertical([column, row + 1], grid)  # recursion

    return aligned


def count_right_up(coordinates, grid):
    """
    Counts diagonal alignments for the given point in right-up direction
    :param coordinates: the coordinates of the cell in the grid
    :param grid: the list representing the board(grid) which is being played on
    :return: the number of cells with the same discs aligned to the right-up
    """
    aligned = 1
    column, row = coordinates

    if grid[row][column] == grid[row + 1][column + 1]:
        aligned += count_right_up([column + 1, row + 1], grid)

    return aligned


def count_right_down(coordinates, grid):
    """
    Counts diagonal alignments for the given point in right-down direction
    :param coordinates: the coordinates of the cell in the grid
    :param grid: the list representing the board(grid) which is being played on
    :return: the number of cells with the same discs aligned to the right-down
    """
    aligned = 1
    column, row = coordinates

    if grid[row][column] == grid[row - 1][column + 1]:
        aligned += count_right_down([column - 1, row + 1], grid)

    return aligned


def find_max_aligned(disc, grid):
    """
    Counts maximal number of aligned discs on the board
    :param disc: the disc to check the maximal aligned for ('*' or '0')
    :param grid: the list representing the board(grid) which is being played on
    :return: maximal number aligned discs (for given discs)
    """
    aligned = [0]
    for x in COLUMNS:  # checks every cell
        for y in ROWS:
            if grid[y][x] == disc:
                # checks every direction
                aligned.append(count_horizontal([x, y], grid))
                aligned.append(count_vertical([x, y], grid))
                aligned.append(count_right_up([x, y], grid))
                aligned.append(count_right_down([x, y], grid))

    return max(aligned)  # returns maximal
