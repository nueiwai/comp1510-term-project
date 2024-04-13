import random
"""
This module contains:

Games:
- Base Conversion: Converts decimal numbers to other bases.
- Roman Numeral Conversion: Translates decimal numbers into Roman numerals.
- Caesar Cipher: Enciphers or deciphers messages using the Caesar cipher.

Functions:
- Conversion Functions for Games: `decimal_to_base()`, `roman_numeral_converter()`, `caesarcipher()`
- Game Drivers: `play_base_conversion_game()`, `play_roman_numeral_conversion_game()`, `play_caesar_cipher_game()`
- Support Functions: Functions for generating question choices and validating player responses for each game.
"""


def decimal_to_base(decimal_num, base):
    """
    Convert a decimal number to a desired base with up to 4 digits.

    :param decimal_num: Decimal number to convert
    :param base: base to convert to
    :precondition: decimal_num must be a non-negative integer
    :precondition: base must be an int in range [2, 9]
    :postcondition: convert the decimal number to a string representing the number in the specified base
    :return: converted number as a string

    >>> decimal_to_base(15, 2)
    '1111'

    >>> decimal_to_base(10, 8)
    '12'
    """
    if decimal_num == 0:
        return "0"

    result = ""
    while decimal_num > 0:
        result = str(decimal_num % base) + result
        decimal_num //= base

    return result


def generate_choices_for_base_conversion(correct_answer, base):
    """
    Generate a list of multiple choice answers for a base conversion game, including the correct answer and two fake
    answers.

    :param correct_answer: the correct answer for the base conversion game
    :param base: the base to which the decimal number should be converted
    :precondition: correct_answer must be a string representing the correct answer
    :precondition: base must be an integer in the range [2, 9]
    :postcondition: generate two fake answers for the base conversion game and shuffle them with the correct answer
    :return: a list of tuples, where each tuple contains an integer (starting from 1) and a string message. This list
            contains exactly three unique messages including the correct one
    """
    base_conversion_variations = [correct_answer]
    # Generate two more unique base_conversion_variations
    while len(base_conversion_variations) < 3:
        choice = correct_answer
        alter_position = random.randint(0, len(correct_answer) - 1)  # Randomly choose a position to change
        new_digit = str(random.choice([digit for digit in range(base) if str(digit) != correct_answer[alter_position]]))
        choice = choice[:alter_position] + new_digit + choice[alter_position+1:]  # Replace the digit in alter_position
        if choice not in base_conversion_variations:
            base_conversion_variations.append(choice)
    random.shuffle(base_conversion_variations)

    choices_base_conversion = list(enumerate(base_conversion_variations, 1))
    return choices_base_conversion


def play_base_conversion_game(player, number_upperbound, base_upperbound):
    """
    Run a game where the player converts a decimal number to a specified base.

    :param player: A dictionary containing the player's attributes
    :param number_upperbound: the upper limit for the randomly generated decimal number
    :param base_upperbound: the upper limit for the base to which the decimal number should be converted
    :precondition: gpa must be a float representing the player's current GPA
    :precondition: number_upperbound must be an integer greater than 1
    :precondition: base_upperbound must be an integer between 2 and 9 (2, 9]
    :postcondition: generate the question according to provided bounds, check the player's answer and if the player's
                    answer is incorrect, their GPA decreases by 0.05
    :return: the updated player dictionary after evaluating the player's answer
    """
    # Upperbound is adjusted according to level
    decimal_number = random.randint(1, number_upperbound)
    # Upperbound is adjusted according to level
    base = random.randint(2, base_upperbound)
    correct_answer = decimal_to_base(decimal_number, base)
    choices = generate_choices_for_base_conversion(correct_answer, base)
    print(f"Convert the number {decimal_number} to base {base}. Here are your options:")
    get_player_choice_and_evaluate(choices, correct_answer, player)
    return player


def roman_numeral_converter(number):
    """
    Convert a number into a roman numeral by calling other functions.

    :param number: the number which is needed to be converted to roman numeral
    :precondition: the number must be positive int in the range [1,5000]
    :postcondition: convert each digit in the number into corresponding roman numeral correctly
    :postcondition: concatenate the converted letters representing the digits in correct order
    :return: return the converted roman numeral of the number as a whole as str

    >>> roman_numeral_converter(123)
    'CXXIII'
    >>> roman_numeral_converter(5000)
    'MMMMM'
    >>> roman_numeral_converter(1)
    'I'
    """
    # list of roman numerals grouped by positional value
    roman_numeral = [["", "M", "MM", "MMM", "MMMM", "MMMMM"],
                     ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                     ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                     ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]]

    # find digits for each positions in the given number
    thousands_digit = number // 1000
    hundreds_digit = (number % 1000) // 100
    tens_digit = (number % 100) // 10
    ones_digit = (number % 10) // 1

    # fetch each digit corresponding roman numeral and concatenate them into a string
    result = (roman_numeral[0][thousands_digit] + roman_numeral[1][hundreds_digit] +
              roman_numeral[2][tens_digit] + roman_numeral[3][ones_digit])

    return str(result)


def generate_choices_for_roman_numeral(correct_answer, org_number):
    """
    Generate a list of multiple choice answers for a Roman numeral conversion game, including the correct answer and two
    fake Roman numerals.

    :param correct_answer: the correct Roman numeral for the given number
    :param org_number: the original number for which the correct_answer is generated
    :precondition: correct_answer must be a string representing the correct Roman numeral for the org_number
    :precondition: org_number must be an integer in the range [1, 5000]
    :postcondition: generate two fake Roman numerals for the org_number and shuffle them with the correct_answer
    :postcondition: return a list of tuples, each containing an index and a Roman numeral, with the numerals shuffled
    :return: a list of tuples, where each tuple contains an integer (starting from 1) and a string message. This list
            contains exactly three unique messages including the correct one


    """
    roman_numeral_variations = [correct_answer]
    while len(roman_numeral_variations) < 3:
        # Generate a random number close to the original number for plausible incorrect answers
        range_for_answer_variations = random.randint(-5, 5)
        # While answer is out of bound or already in roman_numeral_variations, generate a new random number  variations
        while (org_number + range_for_answer_variations < 1 or org_number + range_for_answer_variations > 5000 or
               roman_numeral_converter(org_number + range_for_answer_variations) in roman_numeral_variations):
            range_for_answer_variations = random.randint(-5, 5)
        choice = roman_numeral_converter(org_number + range_for_answer_variations)
        roman_numeral_variations.append(choice)
    random.shuffle(roman_numeral_variations)

    choices_roman_numeral = list(enumerate(roman_numeral_variations, 1))
    return choices_roman_numeral


def play_roman_numeral_conversion_game(player, target_num_upbound):
    """
    Run a game where the player must convert a randomly generated decimal number to its Roman numeral.

    :param player: A dictionary containing the player's attributes
    :param target_num_upbound: the upper limit for generating the decimal number for conversion
    :precondition: gpa must be a floating-point number
    :precondition: target_num_upbound must be an integer greater than 1
    :postcondition: generate the question according to provided bounds, check the player's answer and if the player's
                    answer is incorrect, their GPA decreases by 0.05
    :return: the updated player dictionary after evaluating the player's answer
    """
    print("You will need to answer the correct numeral!!")

    # Generate a random number for the game (upperbound to be adjusted according to level)
    target_number = random.randint(1, target_num_upbound)
    correct_answer = roman_numeral_converter(target_number)
    choices = generate_choices_for_roman_numeral(correct_answer, target_number)
    print(f"Convert the number {target_number} to a Roman numeral. Here are your options:")
    get_player_choice_and_evaluate(choices, correct_answer, player)
    return player


def caesarcipher(message, encode, shift):
    """
    Encrypt or decrypt a given message using Caesar Cipher.

    param message: the message to be encrypted or decrypted
    param encode: the indicator to encrypt(True) or decrypt(False) the message
    param shift: the key value to do the shifting with
    precondition: message must be a string
    precondition: encode must be a boolean value
    precondition: shift must be an integer
    postcondition: the message is encrypted or decrypted
    return: the encrypted or decrypted message as string

    >>> caesarcipher("I am going to finish this !! __", True, 6)
    'O gs muotm zu lotoyn znoy !! __'
    >>> caesarcipher("tew", False, -10)
    'dog'
    """
    converted_msg = ""
    for character in message:
        # condition for characters which are uppercase alphabets and encode == True
        if character.isalpha() and character.isupper() and encode:
            converted_msg += chr(((ord(character) - ord("A")) + shift) % 26 + ord("A"))

        # condition for characters which are lowercase alphabets and encode == True
        elif character.isalpha() and character.islower() and encode:
            converted_msg += chr(((ord(character) - ord("a")) + shift) % 26 + ord("a"))

        # condition for characters which are uppercase alphabets and encode == False
        elif character.isalpha() and character.isupper() and not encode:
            converted_msg += chr(((ord(character) - ord("A")) - shift) % 26 + ord("A"))

        # condition for characters which are lowercase alphabets and encode == False
        elif character.isalpha() and character.islower() and not encode:
            converted_msg += chr(((ord(character) - ord("a")) - shift) % 26 + ord("a"))

        # condition for all other characters
        else:
            converted_msg += character
    return converted_msg


def select_message_list(term):
    """
    Select a list of messages based on the provided term.

    :param term: an integer representing the terml (1 to 4)
    :precondition: term must be an integer between 1 and 4, inclusive
    :postcondition: a list corresponding to the chosen term is returned
    :return: a list of messages corresponding to the chosen term level

    """
    term1 = ["Cat", "Dog", "Mop", "Hot", "Sun", "Was", "Pie", "Rio", "bat", "hog", "top", "cot", "hat", "fox", "pot",
             "rat", "log", "pop", "bit", "sob", "jet", "rub", "dip", "hum", "lot", "gap", "fib", "wet"]
    term2 = ["Great Wall", "Magic Wand", "Heavy Rain", "Sweet Home", "White Gate", "Royal Port", "Sharp Turn",
             "Black Pool", "Light Snow", "Grand Hall", "Green Park", "Quick Sand", "Small Pond", "Large Rock",
             "Brave Soul", "Clear Path", "Brown Bear", "Fresh Fish", "Proud Lion", "Round Lake"]
    term3 = ["Summer Sun", "Forest Owl", "Public Eye", "Silver Fox", "Golden Key", "Frozen Air", "Travel Map",
             "Wintery Mix", "Window Bay", "Market Day", "Flower Pot", "Master Key", "Jungle Cat", "Garden Hoe",
             "Coffee Mug", "Pillow Top", "Dinner Set", "Office Pen", "Dessert Bar", "Candle Wax"]
    term4 = ["Feedback Loop", "Breakfast Nook", "Colorful Bird", "Mountain Peak", "American Eagle",  "Sunflower Seed",
             "Overnight Stay", "Homeschool Room", "Waterfall Drop", "Elevator Shaft", "Underpass Road",
             "Butterfly Wing", "Crossover Gate", "Telescope Lens", "Riverbank Edge", "Chocolate Cake",
             "Grasslands Park", "Crossroad Path", "Staircase Rise", "Lightning Bolt"]

    if term == 1:
        return term1
    elif term == 2:
        return term2
    elif term == 3:
        return term3
    elif term == 4:
        return term4


def generate_caesar_cipher_variations(correct_message, all_messages):
    """
    Generate a list of multiple choice answers for a Caesar cipher game, including the correct answer and two fake
    messages.

    :param correct_message: a correct decrypted message.
    :param all_messages: a list of potential decrypted messages which includes the correct message
    :precondition: 'correct_message' must be a string and should be an element of 'all_messages'
    :precondition: 'all_messages' must be a list of strings with at least two unique elements besides 'correct_message'.
    :postcondition: returns a list of tuples, each containing an index and a message, with the messages shuffled to
                    provide random order of choices
    :return: a list of tuples, where each tuple contains an integer (starting from 1) and a string message. This list
            contains exactly three unique messages including the correct one

    """
    caesarcipher_variations = [correct_message]  # Include the correct answer
    while len(caesarcipher_variations) < 3:
        fake_message = random.choice(all_messages)
        if fake_message not in caesarcipher_variations and fake_message != correct_message:
            caesarcipher_variations.append(fake_message)
    random.shuffle(caesarcipher_variations)

    choices_caesarcipher = list(enumerate(caesarcipher_variations, 1))
    return choices_caesarcipher


def play_caesar_cipher_game(player, term, shift_limit):
    """
    Run a Caesar Cipher decryption game where a player attempts to decrypt an encrypted message using provided key.

    :param player: A dictionary containing the player's attributes
    :param term: term no. indicating the difficulty level
    :param shift_limit: The maximum shift value for the Caesar cipher
    :precondition: gpa must be a float representing the player's current GPA
    :precondition: term should be an integer between 1 and 4, inclusive
    :precondition: shift_limit must be an integer greater than 0
    :postcondition: generate the question according to provided bounds, check the player's answer and if the player's
                    answer is incorrect, their GPA decreases by 0.05
    :return: the updated player dictionary after evaluating the player's answer
    """
    print("Welcome. You will need to play the Caesar Cipher Decryption Game!")

    # Choose a message from a message list (term must be adjusted according to the level)
    messages = select_message_list(term)
    original_message = random.choice(messages)
    # Shift can be adjusted according to the level
    shift = random.randint(1, shift_limit)
    encrypted_message = caesarcipher(original_message, True, shift)

    print(f"Try to Decrypt this message (key = {shift}: {encrypted_message}. Your options are:")
    message_choices = generate_caesar_cipher_variations(original_message, messages)
    get_player_choice_and_evaluate(message_choices, original_message, player)
    return player


def get_player_choice_and_evaluate(choices, correct_answer, player):
    """
    Prompt the player to choose an answer from the given choices, validate the input, and evaluate the choice.

    :param choices: A dictionary with choice labels (e.g., "A", "B", "C") to their corresponding answers
    :param correct_answer: The correct answer string
    :param player: A dictionary containing the player's attributes
    :precondition: choices and correct_answer must be a non-empty string
    :postcondition: get player's choice from input and compare it with correct answer and adjust player's gpa
    :return: player's updated gpa
    """
    choices_allowed = dict()
    for key, value in choices:
        print(f"{key}: {value}")
        choices_allowed.update({key: value})

    while True:
        try:
            player_choice = input("Choose your answer (1, 2, 3): ").strip()
            if not player_choice.isdigit() or player_choice == '':
                raise ValueError("Input must be a non-empty numeric string (1, 2, or 3).")
            if int(player_choice) not in choices_allowed:
                raise ValueError("Invalid choice. Please select 1, 2, or 3.")
            break
        except ValueError as error:
            print(error)

    # Evaluate the player's choice after a valid input
    if choices_allowed[int(player_choice)] == correct_answer:
        print("Correct! Well done. Keep up the good work.")
        return player
    else:
        player["GPA"] -= 0.05  # Decrease GPA by 0.05 for an incorrect guess
        print(f"Incorrect! The correct answer was {correct_answer}.")
        print(f"Your GPA has decreased to {player["GPA"]:.2f}")
        return player


if __name__ == "__main__":
    play_base_conversion_game(4.0, 125, 3)
    play_roman_numeral_conversion_game(4.0, 10)
    play_caesar_cipher_game(3.45, 1, 2)
