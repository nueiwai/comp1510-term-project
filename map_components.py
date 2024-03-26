def make_board(rows, columns):
    board = {(x_coordinate, y_coordinate): "Empty" for x_coordinate in range(columns) for y_coordinate in range(rows)}
    board[(24, 1)] = "Start of term 2"
    board[(0, 2)] = "Start of term 3"
    board[(24, 3)] = "Start of term 4"
    board[(0, 3)] = "The end of the program"
    print(board)
    return board


def display_board(board, character):
    columns = max(key[0] for key in board.keys()) + 1
    rows = max(key[1] for key in board.keys()) + 1
    char_col = character["X-coordinate"]
    char_row = character["Y-coordinate"]
    ascii_board = ""

    # Top border of the board
    ascii_board += "╔" + "═══╦" * (columns - 1) + "═══╗\n"

    for row in range(rows):
        # Left border of the row
        row_str = "║"
        for col in range(columns):
            if row == char_row and col == char_col:
                # Character
                cell = "@"
            else:
                # Empty cell
                cell = " "
            # left and right padding and the content
            row_str += f" {cell} "
            if col < columns - 1:
                # Middle border between cells
                row_str += "║"
        # Right border of the row
        row_str += "║\n"

        # Add the row to the board
        ascii_board += row_str

        # Middle borders between rows
        if row < rows - 1:
            ascii_board += "╠" + ("═══╬" * (columns - 1)) + "═══╣\n"

    # Bottom border of the board
    ascii_board += "╚" + "═══╩" * (columns - 1) + "═══╝\n"

    return ascii_board


def describe_current_position(player, board):
    print(f"You are at {board[(player["X-coordinate"], player["Y-coordinate"])]}")


def main():
    board = make_board(4, 25)
    print(display_board(board, {"X-coordinate": 24, "Y-coordinate": 1, "GPA": 2.0}))


if __name__ == "__main__":
    main()