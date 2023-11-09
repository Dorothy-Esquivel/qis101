#!/usr/bin/env python3
"""connect_four.py"""

# Entirely used Dave's code


def check_ray(board: list[list[int]], row: int, col: int) -> bool:
    """Check if the current position (row,col) forms a winning combination in any direction."""

    # Check diagnoals going upwards.
    if row > 2:
        if col < 4 and (
            # Checks if the value at the current position is the same as the value in the cell diagonally one row above and one col to the right.
            board[row][col] == board[row - 1][col + 1]
            # Checks if the value at the current position is the same as the value in the cell diagonally two rows above and two col to the right.
            and board[row][col] == board[row - 2][col + 2]
            # Checks if the value at the current position is the same as the value in the cell diagonally three rows above and three col to the right.
            and board[row][col] == board[row - 3][col + 3]
        ):
            return True
        if col > 2 and (
            # Refer to lines 12, 14, and 16 to under stand the next 3 lines of code and so on.
            board[row][col] == board[row - 1][col - 1]
            and board[row][col] == board[row - 2][col - 2]
            and board[row][col] == board[row - 3][col - 3]
        ):
            return True
        if (
            board[row][col] == board[row - 1][col]
            and board[row][col] == board[row - 2][col]
            and board[row][col] == board[row - 3][col]
        ):
            return True
    # Check diagonals going downwards.
    if row < 3:
        if col < 4 and (
            board[row][col] == board[row + 1][col + 1]
            and board[row][col] == board[row + 2][col + 2]
            and board[row][col] == board[row + 3][col + 3]
        ):
            return True
        if col < 2 and (
            board[row][col] == board[row + 1][col - 1]
            and board[row][col] == board[row + 2][col - 2]
            and board[row][col] == board[row + 3][col - 3]
        ):
            return True
        if (
            board[row][col] == board[row + 1][col]
            and board[row][col] == board[row + 2][col]
            and board[row][col] == board[row + 3][col]
        ):
            return True
    # Check horizontal and vertical directions.
    if col < 4 and (
        board[row][col] == board[row][col + 1]
        and board[row][col] == board[row][col + 2]
        and board[row][col] == board[row][col + 3]
    ):
        return True
    if col > 2 and (
        board[row][col] == board[row][col - 1]
        and board[row][col] == board[row][col - 2]
        and board[row][col] == board[row][col - 3]
    ):
        return True
    # No winning combination found.
    return False


def check_winner(player: int, board: list[list[int]]) -> bool:
    """Check if the specified player has won the game"""

    # Iterate over each position on the board. Specifying on how the board is organized: the top left of the board is at position(row(0),col(0)).
    # Continuing on down the row: position(row(0),col(1)), positin(row(0), col(2)), etc.
    for row in range(6):
        for col in range(7):
            # If the current position matches the player and forms a winning combination, return True.
            if board[row][col] == player and check_ray(board, row, col):
                return True
    # No winner found.
    return False


def print_winner(board: list[list[int]]) -> None:
    """Print the board and the winner (if any)."""
    print(*board, sep="\n")

    # Checks for a winner.
    if check_winner(1, board):
        print("Player 1 wins!")
    else:
        if check_winner(2, board):
            print("Player 2 wins!")
        else:
            print("No winner yet.")
    print()


def main() -> None:
    """Defines different game boards and prints the winner(if any)."""
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)
    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)
    board3: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


if __name__ == "__main__":
    main()
