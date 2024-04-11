import final_boss
"""
This module contains:

The scaled version of the final boss (challenge) of our game in the form of a job interview post-graduation.
The executed code snippets is now intended to "answer" the questions posed by the interviewer.
"""


def job_interview_intro():
    """
    Print the intro message to the first job interview after graduation from CST.

    >>> job_interview_intro()
    Welcome to your first job interview.
    To hopefully receive a job offer follow these instructions to the best of your abilities.
    <BLANKLINE>
    Write code that results in the answer to the question the interviewer is asking.
    Remember not only does your code need to successfully execute, it needs to answer the question
    When you're done choosing your lines of code, enter 'e' (for execute of course) to execute selections.
    """
    print(f"Welcome to your first job interview.")
    print(f"To hopefully receive a job offer follow these instructions to the best of your abilities.")
    print(f"\nWrite code that results in the answer to the question the interviewer is asking.")
    print(f"Remember not only does your code need to successfully execute, it needs to answer the question")
    print(f"When you're done choosing your lines of code, enter 'e' (for execute of course) to execute selections.")


def generate_code_snippet_options_for_interview(question_completed):
    """
    Generate the available list of code snippets for the player to choose from for the interview.

    :param question_completed: a positive integer from 1 to 3
    :return: a list of code snippets representing the available options for the given question
    """
    question_1 = [
        f"years = 8 % 3\n",
        f"print(years)\n",
        f"nolan, spring = 3, 2\n",
        f"years = nolan // spring if nolan * spring > 0 else (nolan + (-nolan % spring)) // spring\n",
        f"years = int(-1 / 2)\n"
    ]
    question_2 = [
        f"if __name__ == '__main__':\n\t",
        f"main()\n",
        f"def print_watcher(func):\n\t",
        f"def wrapper_print_watcher(*args, **kwargs):\n\t\t",
        f"func(*args, **kwargs)\n\t",
        f"return wrapper_print_watcher\n\n",
        f"@print_watcher\n",
        f"def print_food(food):\n\t",
        f"print('The ' + food + ' on the table!')\n\n",
        f"def main():\n\t",
        f"print_food('feijoada')\n\n"
    ]
    question_3 = [
        f"loyalty_in_question = all(loyalty)\n",
        f"print(loyalty_in_question)\n",
        f"loyalty = [True, True, True, False]\n"
    ]

    if question_completed == 1:
        return question_1
    elif question_completed == 2:
        return question_2
    elif question_completed == 3:
        return question_3


def select_interview_question(question_completed):
    """
    Select from three interview questions to display to interviewee in order.

    :param question_completed: a positive integer from 1 to 3
    :return: a tuple containing the correct answer to the question and a message from the interviewer

    >>> select_interview_question(1)
    <BLANKLINE>
    Interviewer: How many years did it take you to graduate CST?
    (2, 'Hm! You graduated on time, good for you. Next question.')
    >>> select_interview_question(2)
    <BLANKLINE>
    Interviewer: What is the lost dog looking at?
    ('The feijoada on the table!', 'Interesting, did not think you would get that one right. Last question.')
    >>> select_interview_question(3)
    <BLANKLINE>
    Interviewer: True or false? Are you willing to work overtime?
    (False, 'You passed the interview. 🤯')
    """
    if question_completed == 1:
        print(f"\nInterviewer: How many years did it take you to graduate CST?")
        correct_answer = 2
        interviewer_message = f"Hm! You graduated on time, good for you. Next question."
        return int(correct_answer), interviewer_message
    elif question_completed == 2:
        print(f"\nInterviewer: What is the lost dog looking at?")
        correct_answer = f"The feijoada on the table!"
        interviewer_message = f"Interesting, did not think you would get that one right. Last question."
        return correct_answer, interviewer_message
    elif question_completed == 3:
        print(f"\nInterviewer: True or false? Are you willing to work overtime?")
        correct_answer = False
        interviewer_message = f"You passed the interview. 🤯"
        return bool(correct_answer), interviewer_message


def job_interview():
    """
    Drive the main function for the final boss challenge.
    """
    job_interview_intro()
    # initiate count of interview questions completed
    question_completed = 0
    while question_completed < 3:
        question_completed += 1
        correct_answer, interviewer_message = select_interview_question(question_completed)
        code_snippets = generate_code_snippet_options_for_interview(question_completed)
        chosen_snippets = final_boss.get_player_choice(code_snippets)
        try:
            correct_answer == final_boss.execute_chosen_code_snippets(chosen_snippets)
        except ValueError:
            print(f"Code snippet crashed due to ValueError. Failed interview.")
            break
        except NameError:
            print(f"Code snippet crashed due to NameError. Failed interview.")
            break
        else:
            print(f"🐢 🐢 🐢 🐢 🐢 🐢 🐢 🐢 🐢 🐢")
            print(interviewer_message)


if __name__ == "__main__":
    job_interview()
