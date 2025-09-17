from random import randint

from brain_games.utils import is_even


def game():
    question = number = randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return {
        "question": question,
        "answer": correct_answer
    }
