from random import randint
from align_counter import find_max_aligned, ROWS, COLUMNS

EMPTY_GRID = [
    # This list represents an empty board(grid)
    # Note: this object must not be changed
    # Note: usually in python variables that should stay constant are
    # named with caps just for programmers to know that it is constant,
    # and it should not be changed
    # Note: for user it will be displayed 'upside-down'
    [' ', '1', '2', '3', '4', '5', '6', '7', ' '],
    ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
    ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2'],
    ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '3'],
    ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '4'],
    ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '5'],
    ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '6'],
    [' ', '1', '2', '3', '4', '5', '6', '7', ' ']
]


def new_board():  # ex 2
    """
    Returns a copy of 'EMPTY_GRID';
    Used to get a new empty board before starting the game

    :return: empty grid
    """
    grid = []
    # the global variable 'EMPTY_GRID' should always stay the same
    # so that we can't just write 'grid = EMPTY_GRID' or 'return EMPTY_GRID'
    for row in EMPTY_GRID:
        grid.append(row.copy())

    return grid


def display(grid: list):
    """
    Displays the board(grid)
    :param grid: the list representing the board(grid) which is being played on
    :return: None
    """
    for row in grid[::-1]:
        for cell in row:
            print(cell, end=' ')
        print()  # go to the next line


def is_possible(column, grid):
    """
    Checks whether the turn is possible
    :param column: column to check if it's possible to play in
    :param grid: the list representing the board(grid) which is being played on
    :return: True if turn is possible, False if not
    """
    if COLUMNS[0] <= column <= COLUMNS[-1]:  # checks if the column exists
        # if the last column is free, then there is at least one free column, else there are no
        if grid[ROWS[-1]][column] == ' ':
            return True
        else:
            return False
    else:
        return False


def drop(disc: str, column: int, grid: list):
    """
    Drops a disc into the given column
    :param disc: the disc to drop ('*' or '0') (actually can be any single-character string)
    :param column: a column to drop the disc into
    :param grid: the list representing the board(grid) which is being played on
    :return: None
    """
    for row in ROWS:
        if grid[row][column] == ' ':
            grid[row][column] = disc
            return


def remove_disc(column, grid):
    """
    Removes the last dropped disc from the column
    :param column: a column to remove the disc from
    :param grid: the list representing the board(grid) which is being played on
    :return: None
    """
    if not COLUMNS[0] <= column <= COLUMNS[-1]:  # if given column is out of range
        return
    for row in ROWS[::-1]:
        if grid[row][column] != ' ':
            grid[row][column] = ' '
            return


def get_key(value, dictionary):
    """
    Gets the first key referring to the given value in the dictionary
    :param value: value to find its key
    :param dictionary: dictionary in where to seek the key
    :return: first key with the given value
    """
    for key in dictionary.keys():
        if dictionary[key] == value:
            return key


def random_advice(grid):
    """
    Offers a random possible column to make a turn

    :param grid: the list representing the board(grid) which is being played on
    :return: a random possible column to make a turn
    """
    while True:
        column = randint(COLUMNS[0], COLUMNS[-1])
        if is_possible(column, grid):
            return column


def find_best_turn(disc, grid):
    """
    Finds out the column to play in to make the best turn in case of making maximal aligned disks

    :param disc: the disc to check the best turn for ('*' or '0')
    :param grid: the list representing the board(grid) which is being played on
    :return: the column to play in to make the best turn
    """
    aligned = dict()

    for column in COLUMNS:  # tries each column to find the best turn
        if is_possible(column, grid):
            drop(disc, column, grid)  # drops a disc to check
            aligned.update({column: find_max_aligned(disc, grid)})  # adds the value of max aligned in this case
            remove_disc(column, grid)  # removes the disc

    if all(aligned.values()) == max(aligned.values()):  # if all the turns lead to the same result
        column = random_advice(grid)  # the column will be chosen randomly
    else:
        column = get_key(max(aligned.values()), aligned)  # else, returns the best variant(or one of the best)

    return column


def computer_plays(disc, grid):
    """
    Computer makes a turn

    :param disc: the disc to check the best turn for ('*' or '0')
    :param grid: the list representing the board(grid) which is being played on
    :return: None
    """
    column = find_best_turn(disc, grid)
    drop(disc, column, grid)


def user_plays(disc, grid):
    """
    Lets user make a turn

    :param disc: the disc to check the best turn for ('*' or '0')
    :param grid: the list representing the board(grid) which is being played on
    :return: None
    """
    input_column = input('Enter the number of column to drop the disc in: ')
    try:
        column = int(input_column)
        if is_possible(column, grid):
            drop(disc, column, grid)
        else:
            print('Turn is impossible')
            print('Choose the columns from 1 to 7 with free cells')
            user_plays(disc, grid)
    except ValueError:
        print('Wrong input')
        print('Should be an integer between 1 and 7')
        user_plays(disc, grid)


def win(disc, grid):
    """
    Lets user make a turn
    :param disc: the disc to check the best turn for ('*' or '0')
    :param grid: the list representing the board(grid) which is being played on
    :return: True if the given disk wins, False if not
    """
    if find_max_aligned(disc, grid) >= 4:
        return True
    else:
        return False


def user_vs_computer(grid):
    """
    Lets user play with computer
    :param grid: the list representing the board(grid) which is being played on
    :return: None
    """
    user, computer = '*', '0'  # could be the opposite way as well
    display(grid)

    while True:
        user_plays(user, grid)
        display(grid)
        if win(user, grid):
            print('You won!')
            break

        computer_plays(computer, grid)
        display(grid)
        if win(computer, grid):
            print('Computer won!')
            break


if __name__ == '__main__':
    board = new_board()
    user_vs_computer(board)
