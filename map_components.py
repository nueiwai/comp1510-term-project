def generate_term_map(total_cell):
    """
    Generate a dictionary of cell numbers as keys their respective term, day of term, and week of term as value.

    :param total_cell: total number of cells to be included in the dictionary
    :precondition: total_cell must be a positive int
    :postcondition: create a dictionary which has cell numbers from 1 to total_cell inclusively as "key" and for value
                    it will contain a list of term number in range [1, 4], day of term in range [1 to 25] and
                    week of term (5 days == 2 weeks) in range [1 to 10]
    :return: a dictionary where keys are cell numbers and values are lists containing the term, day of term, and week
             of term

    >>> result = generate_term_map(100)
    >>> result[1]
    [1, 1, 1]
    >>> result[50]
    [2, 25, 10]

    """
    term_map = {}
    for cell_number in range(1, total_cell + 1):
        term = (cell_number - 1) // 25 + 1  # Calculate term
        day_of_term = (cell_number - 1) % 25 + 1  # Calculate day of term
        week_of_term = int((day_of_term - 1) // 2.5) + 1  # Calculate week of term [5 days (cells) == 2 weeks]
        term_map[cell_number] = [term, day_of_term, week_of_term]  # Assign the list respective map key
    return term_map


def add_term_information_to_map(row_content, cell, term_starting_cells):
    """
    Append term information to a given row content string based on the cell number.

    :param row_content: a str representing the contents of the whole row in map
    :param cell: a cell number that program is working on
    :param term_starting_cells: a list of numbers representing the cells number where each cell represent the starting
                                of a term
    :precondition: term_starting_cells list must contain int representing the starting cells of terms in ascending order
    :precondition: cell must be an int representing the current cell number
    :postcondition: add term information if the cell is starting cell of a term, otherwise, add spaces
    :return: the updated row content str with term information appended

    """
    if cell in term_starting_cells:
        term_num = term_starting_cells.index(cell) + 1
        row_content += "║{:^7}".format("Term" + str(term_num))
    else:
        row_content += "║       "
    return row_content


def add_player_location_to_map(row_content, cell, player):
    """
    Append the player's location indicator to the row content if the current cell is the player's location.

    :param row_content: a str representing the contents of the whole row in map
    :param cell: a cell number that program is working on
    :param player: a dictionary which includes a key "location" indicating the player's current location
    :precondition: player must be a dictionary which includes a key "location" whose value is an int
    :precondition: cell must be an int representing the current cell number
    :postcondition: add an indicator to represent the player's location to the row content if the cell matches the
                    player's location, otherwise add spaces
    :return: the updated row content str with the player's location indicator

    """
    if cell == player["location"]:
        row_content += "║{:^7}".format("𒊹")
    else:
        row_content += "║       "
    return row_content


# Generate row content
def generate_row_content_for_map(row, columns, term_starting_cells, player):
    """
    Generate the contents of a row in the game map: cell numbers, term information, and player location.

    :param row: current row number
    :param columns: total number of columns in the game map.
    :param term_starting_cells: a list of int representing the starting cell numbers of each term
    :param player: a dictionary representing the player, including their location
    :precondition: row and columns must be ints representing valid positions within the game map
    :precondition: term_starting_cells must be a list of int indicating the starting cells of each term
    :precondition: player must be a dictionary which includes a key "location" whose value is an int
    :postcondition: complete a str that contains cell numbers, term information, and player location for the row
    :return: a str representing the content of a row in the game map

    """
    row_content = ""  # Initialize the string for the contents of current row
    if row % 2 == 0:
        cells_in_row = [(row * columns + col + 1) for col in range(columns)]  # Cells are numbered left to right
    else:
        cells_in_row = [((row + 1) * columns - col) for col in range(columns)]  # Cells are numbered right to left

    for section in range(3):  # Divide each cells three sessions: cell numbers, Term and player location
        for cell in cells_in_row:
            if section == 0:  # Add cell numbers
                row_content += f"║{cell:^7}"
            elif section == 1:  # Add term
                row_content = add_term_information_to_map(row_content, cell, term_starting_cells)
            elif section == 2:  # Mark player's location
                row_content = add_player_location_to_map(row_content, cell, player)
        row_content += "║\n"  # Add right border for each section in a row
    return row_content  # Return the whole row content


def print_game_map(player):
    """
    Print the ASCII representation of the game map including the player's location.

    :param player: a dictionary representing the player's state, including "location"
    :precondition: player must be a dictionary with a key "location" whose value is an int
    :postcondition: create an ASCII game map with terms, cell numbers, and the player's location on it
    :return: a str representing the ASCII game map with the player's location marked

    """
    columns = 25
    rows = 4
    ascii_board = ""
    ascii_board += "╔" + "═══════╦" * (columns - 1) + "═══════╗\n"
    term_starting_cells = [1, 26, 51, 76]
    for row in range(rows):  # Add each row to the board
        ascii_board += generate_row_content_for_map(row, columns, term_starting_cells, player)
        if row < rows - 1:
            ascii_board += "╠" + "═══════╬" * (columns - 1) + "═══════╣\n"  # add borders between each row
        else:
            ascii_board += "╚" + "═══════╩" * (columns - 1) + "═══════╝\n"  # add the bottom border when it's last row

    return ascii_board


def describe_current_location(game__map, player):
    """
    Print a description of the player's current location based on the game map.

    :param game__map: a dictionary which includes cell numbers,term, day, and week information
    :param player: a dictionary with a key "location" indicating the player's current location
    :precondition: game__map must be a dictionary which has int keys representing the cell numbers
    :precondition: player must be a dictionary which has a key "location" whose value is an int
    :postcondition: print the player's current term, day, and week based on their location

    >>> describe_current_location(generate_term_map(100), {"time": 200, "GPA": 2.5, "social": 10, "location": 1})
    You are now on Day: 1, Week: 1 of Term: 1
    >>> describe_current_location(generate_term_map(100), {"time": 200, "GPA": 2.5, "social": 10, "location": 100})
    You are now on Day: 25, Week: 10 of Term: 4
    """
    location = player["location"]  # Retrieve the player's current location
    if location in game__map:  # Check if cell number is in dictionary
        term = game__map[location][0]  # Get term, day and week from dictionary
        day = game__map[location][1]
        week = game__map[location][2]
        print(f"You are now on Day: {day}, Week: {week} of Term: {term}")
    else:
        print("Invalid location.")


def test_run_map():
    game_map = generate_term_map(100)
    player = {"time": 100, "GPA": 1.8, "social": 50, "location": 22}
    print(print_game_map(player))
    describe_current_location(game_map, player)


if __name__ == "__main__":
    test_run_map()
