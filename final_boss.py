"""
This module contains:

The final boss (challenge) of our game. To defeat the final boss, you must select from a list of code snippets
to execute. The code snippet must execute successfully for the boss to be defeated.
"""


def final_boss_intro():
    """
    Print the intro message to the final boss challenge.
    """
    print(f"Congratulations! You've come so far. Welcome (welcome?) to the final boss!")
    print(f"To defeat the boss, try your best to write a piece of code that will execute successfully.")
    print(f"When you're done choosing your lines of code, enter 'e' (for execute of course) to execute selections.")


def generate_code_snippet_options():
    """
    Generate the available list of code snippets for the player to choose from.
    """
    return [
        f"result = math.factorial(5)",
        f"print('Factorial of 5 is:', result)",
        f"import math"
    ]


def display_code_snippet_options(code_snippets):
    """
    Print out a numbered list that displays all the available code snippets for the player to choose from.

    :param code_snippets: a list containing the code snippets available for selection
    """
    print(f"\nAvailable code snippets to choose from:")
    for count, code_snippet in enumerate(code_snippets):
        print(f"{count + 1}. {code_snippet}")


def get_player_choice(code_snippets):
    """
    Ask the player for their ordered choices and store them in a list.

    :param code_snippets: a list containing the code snippets available for selection
    """
    chosen_snippets = []
    while True:
        display_code_snippet_options(code_snippets)
        choice = input(f"Please enter the number of your choice or 'e' to execute your selections: ")
        if choice.lower() == 'e':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(code_snippets):
                chosen_snippets.append(code_snippets[choice - 1])
            else:
                print(f"That was an invalid choice. Please enter a number between 1 and {len(code_snippets)}")
        except ValueError:
            print("That was an invalid input. Please enter a number or 'e'.")
    return chosen_snippets


def execute_chosen_code_snippets(chosen_snippets):
    """
    Execute the code snippets chosen in the order the player chose them, all at once.

    :param chosen_snippets: a list containing the code snippets chosen by the player
    """
    print(f"\nYour selected code snippets executed:")
    for snippet in chosen_snippets:
        exec(snippet)


def final_boss():
    """
    Drive the main function for the final boss challenge.
    """
    final_boss_intro()
    code_snippets = generate_code_snippet_options()
    chosen_snippets = get_player_choice(code_snippets)
    try:
        execute_chosen_code_snippets(chosen_snippets)
    except ValueError:
        print("Code snippet crashed. Failed in defeating the final boss.")
    except NameError:
        print("Code snippet crashed. Failed in defeating the final boss.")
    else:
        print("Final boss defeated.")


if __name__ == "__main__":
    final_boss()
