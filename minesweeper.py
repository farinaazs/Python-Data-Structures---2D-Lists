# ================= Compulsory Task 1: Minesweeper =================
"""
Create a game called minesweeper.

Create a function that takes a grid of # and -, where each hash (#) represents a
mine and each dash (-) represents a mine-free spot.

Return a grid, where each dash is replaced by a digit, indicating the number of
mines immediately adjacent to the spot i.e. (horizontally, vertically, and
diagonally)

Example of an input:
[ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]

Example of the expected output:
[ ["1", "1", "2", "#", "#"],
["1", "#", "3", "3", "2"],
["2", "4", "#", "2", "0"],
["1", "#", "#", "2", "0"],
["1", "2", "2", "1", "0"] ]

Here is a tip. When checking adjacent positions to a specific position in the grid,
the following table might assist you in determining adjacent indexes:

    NW position       = (-1, -1) >> current_row: -1, current_col: -1
    N position        = (-1, 0) >> current_row: - 1, current_col: 0
    NE position       = (-1, 1) >> current_row: -1, current_col: +1
    W position        = (0, -1) >> current_row: 0, current_col: -1
    CURRENT POSITION  = (0, 0) >> current_row, current_col
    E position        = (0, 1) >> current_row: 0, current_col: +1
    SW position       = (1, -1) >> current_row: +1, current_col: -1
    S position        = (1, 0) >> current_row: +1, current_col: 0
    SE position       = (1, 1) >> current_row: +1, current_col: +1

Also ensure that when checking adjacent positions in the grid that you take into
account that on the edges of the grid, you may go out of bounds
"""

# declare variables
empty = 0
mine = "#"
unknown = -1

# solution grid
solution_grid = [[0, 0, 0, "#", "#"],
                 [0, "#", 0, 0, 0],
                 [0, 0, "#", 0, 0],
                 [0, "#", "#", 0, 0],
                 [0, 0, 0, 0, 0]]


# player grid
player_grid = [[-1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1]]

# empty grid displayed to user/player
grid = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]


# checking boundaries
# NW position       = (-1, -1) >> current_row: -1, current_col: -1
# N position        = (-1, 0) >> current_row: - 1, current_col: 0
# NE position       = (-1, 1) >> current_row: -1, current_col: +1
# W position        = (0, -1) >> current_row: 0, current_col: -1
# CURRENT POSITION  = (0, 0) >> current_row, current_col
# E position        = (0, 1) >> current_row: 0, current_col: +1
# SW position       = (1, -1) >> current_row: +1, current_col: -1
# S position        = (1, 0) >> current_row: +1, current_col: 0
# SE position       = (1, 1) >> current_row: +1, current_col: +1
def count(row, col):
    offsets = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    count = 0
    # checking boundaries and edges
    for offset in offsets:
        offset_row = row + offset[0]
        offset_col = col + offset[1]
        if ((offset_row >= 0 and offset_row <= 4) and (offset_col >= 0 and offset_col <= 4)):
            if solution_grid[offset_row][offset_col] == mine:
                count += 1
    return count


# I struggled with this section to count and display the empty cells and count the mines
# I got steer from the following YouTube URL:
# https://www.youtube.com/watch?v=XTT8mXwIGpQ&ab_channel=TokyoEdtech
def guess_row_and_col(row, col):
    if solution_grid[row][col] == mine:
        print("BOOOOOOOMMMM! You hit a mine!\n")
    elif player_grid[row][col] == unknown:
        player_grid[row][col] = count(row, col)
        cells = [(row, col)]
        offsets = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
        while len(cells) > 0:
            cell = cells.pop()
            for offset in offsets:
                row = offset[0] + cell[0]
                col = offset[1] + cell[1]
                if ((row >= 0 and row <= 4) and (col >= 0 and col <= 4)):
                    if ((player_grid[row][col] == unknown) and (solution_grid[row][col] == empty)):
                        player_grid[row][col] = count(row, col)
                        if (row, col) not in cells:
                            cells.append((row, col))
                        else:
                            player_grid[row][col] = count(row, col)
        print("CONGRATULATIONS! You are safe!\n")


# showing grid solution if user does not hit a mine
def show_grid():
    print("-" * 21)
    symbols = {-1: "#"}
    for row in range(len(player_grid)):
        for col in range(len(player_grid[row])):
            value = player_grid[row][col]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = str(value)
            print(f"| {symbol}", end=" ")
        print("|")
        print("-" * 21)


# displaying an empty board in a grid format
def display_board():
    print("-" * 21)
    for row in range(0, 5):
        print("|", end=" ")
        for col in range(0, 5):
            if grid[row][col] == 0:
                print("-", end=" | ")
            else:
                print(grid[row][col], end=" | ")
        print(" ")
        print("-" * 21)


print("\n******************* MINESWEEPER *******************\n")

display_board()  # displaying empty board

# getting the user input for the row and col values to parse through the function calls
row = int(input("\nGuess a row (1-5): ")) - 1
col = int(input("Guess a col (1-5): ")) - 1
print()

# calling function to parse through input values above
guess_row_and_col(row, col)

# show solution grid after the guess_row_and_col(row, col) function was called
show_grid()

# Thank you, Farinaaz :)
