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


def play_base_conversion_game(gpa, number_upperbound, base_upperbound):
    """
    Run a game where the player converts a decimal number to a specified base.

    :param gpa: The player's current GPA
    :param number_upperbound: the upper limit for the randomly generated decimal number
    :param base_upperbound: the upper limit for the base to which the decimal number should be converted
    :precondition: gpa must be a float representing the player's current GPA
    :precondition: number_upperbound must be an integer greater than 1
    :precondition: base_upperbound must be an integer between 2 and 9 (2, 9]
    :postcondition: generate the question according to provided bounds, check the player's answer and if the player's
                    answer is incorrect, their GPA decreases by 0.05
    """
    # Upperbound is adjusted according to level
    decimal_number = random.randint(1, number_upperbound)
    # Upperbound is adjusted according to level
    base = random.randint(2, base_upperbound)
    correct_answer = decimal_to_base(decimal_number, base)
    print(f"Convert the number {decimal_number} to base {base}: ", end="")

    user_answer = input().strip()

    if user_answer == correct_answer:
        print("Correct! Well done. Keep up the good work.")
    else:
        gpa -= 0.05
        print(f"Wrong. The correct answer was {correct_answer}.")
        print(f"Your GPA has decreased to {gpa:.2f}")


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


def play_roman_numeral_conversion_game(gpa, target_num_upbound):
    """
    Run a game where the player must convert a randomly generated decimal number to its Roman numeral.

    :param gpa: player's current GPA
    :param target_num_upbound: the upper limit for generating the decimal number for conversion
    :precondition: gpa must be a floating-point number
    :precondition: target_num_upbound must be an integer greater than 1
    :postcondition: generate the question according to provided bounds, check the player's answer and if the player's
                    answer is incorrect, their GPA decreases by 0.05
    """
    print("You will need to answer the correct numeral!!")

    # Generate a random number for the game (upperbound to be adjusted according to level)
    target_number = random.randint(1, target_num_upbound)
    print(f"Guess the Roman numeral for the number: {target_number}")

    player_guess = input("Enter your guess: ").upper()

    correct_answer = roman_numeral_converter(target_number)

    # Check the player's guess
    if player_guess == correct_answer:
        print("Correct! Well done. Keep up the good work.")
    else:
        gpa -= 0.05  # Decrease GPA by 0.05 for an incorrect guess
        print(f"Incorrect! The correct Roman numeral was {correct_answer}.")
        print(f"Your GPA has decreased to {gpa:.2f}")


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


    >>> select_message_list(1)
    ['Cat', 'Dog', 'Bird', 'Chris']
    >>> select_message_list(4)
    ['Complexity and Algorithms', 'Cloud Computing Introduction', 'Cryptography and Network Security']
    """
    term1 = ["Cat", "Dog", "Bird", "Chris"]
    term2 = ["Red Velvet", "Logic Gates", "Star Wars", "Iron Man"]
    term3 = ["Python Programming", "Caesar Cipher Game", "Encryption and Decryption", "Beauty and the Beast"]
    term4 = ["Complexity and Algorithms", "Cloud Computing Introduction", "Cryptography and Network Security"]

    if term == 1:
        return term1
    elif term == 2:
        return term2
    elif term == 3:
        return term3
    elif term == 4:
        return term4


def play_caesar_cipher_game(gpa, term, shift_limit):
    """
    Run a Caesar Cipher decryption game where a player attempts to decrypt an encrypted message using provided key..

    :param gpa: player's current GPA
    :param term: term no. indicating the difficulty level
    :param shift_limit: The maximum shift value for the Caesar cipher
    :precondition: gpa must be a float representing the player's current GPA
    :precondition: term should be an integer between 1 and 4, inclusive
    :precondition: shift_limit must be an integer greater than 0
    :postcondition: generate the question according to provided bounds, check the player's answer and if the player's
                    answer is incorrect, their GPA decreases by 0.05

    """
    print("Welcome. You will need to play the Caesar Cipher Decryption Game!")

    # Choose a message from a message list (term must be adjusted according to the level)
    messages = select_message_list(term)
    original_message = random.choice(messages)
    # Shift can be adjusted according to the level
    shift = random.randint(0, shift_limit)
    encrypted_message = caesarcipher(original_message, True, shift)

    print(f"Try to Decrypt this message (key = {shift}: {encrypted_message}")

    # Player's attempt to decrypt
    player_decryption = input("Enter your decryption of the message: ")

    # Check if the player's decryption is correct
    if player_decryption.lower() == original_message.lower():
        print("Correct!! Well done, student. Keep up the good work.")
    else:
        gpa -= 0.05
        print(f"Sorry, the correct decryption was: {original_message}")
        print(f"Your GPA has decreased to {gpa:.2f}")


if __name__ == "__main__":
    play_base_conversion_game(4.0, 125, 3)
    play_roman_numeral_conversion_game(4.0, 10)
    play_caesar_cipher_game(4.0, 1, 2)
