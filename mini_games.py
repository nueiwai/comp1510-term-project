import random


def decimal_to_base(decimal_num, base):
    """
    Convert a decimal number to a desired base with up to 4 digits.

    :param decimal_num: Decimal number to convert
    :param base: base to convert to
    :precondition: decimal_num must be a non-negative integer
    :precondition: base must be an int in range [2, 9]
    :postcondition: convert the decimal number to a string representing the number in the specified base
    :return: converted number as a string
    """
    if decimal_num == 0:
        return "0"

    result = ""
    while decimal_num > 0:
        result = str(decimal_num % base) + result
        decimal_num //= base

    return result


def generate_question(max_decimal, bases):
    """
    Generate a random question for the game.

    :param max_decimal: maximum decimal number to generate
    :param bases: list of possible bases to convert to
    :precondition: max_decimal must be a positive integer
    :precondition: bases should be a list containing integers of bases
    :postcondition: make a tuple consisting of a randomly selected decimal number and bases
    :return: Tuple of (decimal number, base to convert to).
    """
    decimal_number = random.randint(0, max_decimal)
    base = random.choice(bases)
    return decimal_number, base


def play_base_conversion_game():
    """
    Run a game that asks the user to convert decimal numbers to desired bases.

    The game poses questions about converting decimal numbers to base, checks answers, and scores the user
    :precondition: user inputs for answers must be numerical strings corresponding to the correct base conversion
    :postcondition: the game completes after asking a fixed number of questions, displaying the user's total score
    """
    score = 0
    total_questions = 1  # Total questions to ask
    max_decimal = 9999
    bases = [2, 3]

    for _ in range(total_questions):
        decimal_number, base = generate_question(max_decimal, bases)
        correct_answer = decimal_to_base(decimal_number, base)
        print(f"Convert the number {decimal_number} to base {base}: ", end="")

        user_answer = input().strip()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was {correct_answer}.")

    print(f"Game over! Your score: {score}/{total_questions}")
