#!/usr/bin/env python3
"""board_encoding.py"""

# Entirely used Dave's code.


def print_board(board_num: int) -> None:
    """Does the computation for each board number."""
    print(f"Board Number: {board_num}")

    # Creates a 3x3 board filled with zeros
    board: list[list[int]] = [[0 for _ in range(3)] for _ in range(3)]

    # Extract the digits of the board number and assign them to board positions
    board[0][0] = board_num % 3  # Assign the rightmost digit to the top-left position
    board_num = board_num // 3  # Discard the rightmost digit
    board[0][1] = board_num % 3  # Assign the nect digit to the top-center position
    board_num = board_num // 3  # Discard the next digit
    board[0][2] = board_num % 3  # Assign the next digit to the top-right position
    board_num = board_num // 3  # Discard the nect digit

    # Repeats the process specified in lines 14-19 for the remaining rows of the board.
    board[1][0] = board_num % 3
    board_num = board_num // 3
    board[1][1] = board_num % 3
    board_num = board_num // 3
    board[1][2] = board_num % 3
    board_num = board_num // 3

    board[2][0] = board_num % 3
    board_num = board_num // 3
    board[2][1] = board_num % 3
    board_num = board_num // 3
    board[2][2] = board_num % 3
    board_num = board_num // 3

    # prints the board using "\n" to skip a line for each row.
    print(*board, sep="\n")
    # prints an empty line
    print()


def main() -> None:
    """Provides the board numbers and positions of X and/or O."""
    # First Board
    print_board(2271)

    # Second Board
    # This expression tells where 2,which represents O, is on the board with row(1)col(1) being point 0 and row(1)col(2) being point 1, etc.
    # It is implied that the untaken spots are zero, which means there is no X or O.
    print_board(2 * (3**2 + 3**4 + 3**6))

    # Third Board
    # This expression is the same as explained in line 47, just inputting 1, which represents X.
    x: int = 1 * (3**1 + 3**4 + 3**5 + 3**6 + 3**8)
    o: int = 2 * (3**0 + 3**2 + 3**3 + 3**7)
    print_board(x + o)


if __name__ == "__main__":
    main()
