
"""
This module contains:

The exam questions of our game. To take the exam, you must select from a list of code snippets
to execute. The code snippet must execute successfully for the player to pass.
"""


def exam_intro():
    """
    Print the intro message to exam.

    >>> exam_intro()
    Congratulations on finishing the term! We are walking towards the exam room as we speak.
    For the exam we are going to scale things up a bit from the quizzes...
    To move on to the next term, try your best to write a piece of code that will execute successfully.
    <BLANKLINE>
    When you're done choosing your lines of code (in order!),
    enter 'e' (for execute of course) to execute selections.
    """
    print(f"Congratulations on finishing the term! We are walking towards the exam room as we speak.")
    print(f"For the exam we are going to scale things up a bit from the quizzes...")
    print(f"To move on to the next term, try your best to write a piece of code that will execute successfully.\n")
    print(f"When you're done choosing your lines of code (in order!),")
    print(f"enter 'e' (for execute of course) to execute selections.")


def generate_code_snippet_options(term):
    """
    Generate the available list of code snippets for the player to choose from.

    >>> generate_code_snippet_options()
    ['result = math.factorial(5)', "print('Factorial of 5 is:', result)", 'import math']
    """
    if term == 1:
        return [
            f"result = math.factorial(5)\n",
            f"print('Factorial of 5 is:', result)\n",
            f"import math\n",
            f"ph = 6\n",
            f"if ph < 7.0:\n\t",
            f"print('It is acidic')"
        ]
    elif term == 2:
        return [
            f"import random\n",
            f"number = random.randint(1, 10)\n",
            f"print('Random number between 1 and 10 is:', number)\n",
            f"temp = 30\n",
            f"if temp > 25:\n\t",
            f"print('It is warm')"
        ]
    elif term == 3:
        return [
            f"import random\n",
            f"number = random.randint(1, 10)\n",
            f"print('Random number between 1 and 10 is:', number)\n",
            f"temp = 30\n",
            f"if temp > 25:\n",
            f"\tprint('It is warm')\n",
            f"else:\n",
            f"\tprint('It is not warm')\n",
            f"for count in range(5):\n",
            f"\tprint('Iteration:', count)"
        ]
    elif term == 4:
        return [
            f"import random\n",
            f"num_list = []\n",
            f"for _ in range(5):\n",
            f"\tnum_list.append(random.randint(1, 10))\n",
            f"print('Random numbers:', num_list)\n",
            f"even_numbers = [num for num in num_list if num % 2 == 0]\n",
            f"print('Even numbers:', even_numbers)\n",
            f"total = sum(num_list)\n",
            f"print('Sum of all numbers:', total)\n",
            f"average = total / len(num_list)\n",
            f"print('Average of numbers:', average)"
        ]


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

    >>> execute_chosen_code_snippets(
    ...     ['import math', 'result = math.factorial(5)', "print('Factorial of 5 is:', result)"])
    <BLANKLINE>
    Your selected code snippets executed:
    Factorial of 5 is: 120
    """
    print(f"\nYour selected code snippets executed:")
    code_string = ""
    for code in chosen_snippets:
        code_string += code
    exec(code_string)


def display_code_snippet_options(code_snippets):
    """
    Print out a numbered list that displays all the available code snippets for the player to choose from.

    :param code_snippets: a list containing the code snippets available for selection

    >>> display_code_snippet_options(
    ...     ['import math', 'result = math.factorial(5)', "print('Factorial of 5 is:', result)"])
    <BLANKLINE>
    Available code snippets to choose from:
    1. import math
    2. result = math.factorial(5)
    3. print('Factorial of 5 is:', result)
    """
    print(f"\nAvailable code snippets to choose from:")
    for count, code_snippet in enumerate(code_snippets):
        print(f"{count + 1}. {code_snippet.strip()}")


def exam(term=4):
    """
    Drive the main function for the final boss challenge.
    """
    exam_intro()
    code_snippets = generate_code_snippet_options(term)
    chosen_snippets = get_player_choice(code_snippets)
    try:
        execute_chosen_code_snippets(chosen_snippets)
    except SyntaxError:
        print(f"Code snippet crashed. failed the term {term} exam.")
        state = False
    except ValueError:
        print(f"Code snippet crashed. failed the term {term} exam.")
        state = False
    except NameError:
        print(f"Code snippet crashed. failed the term {term} exam.")
        state = False
    else:
        print(f"Congratulations. You passed the exam!")
        print(f"Let's move on to the next term.")
        state = True
    return state


if __name__ == "__main__":
    exam()
