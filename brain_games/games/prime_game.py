from random import randint

from brain_games.utils import is_prime_number


def game():
    question = randint(3, 100)
    correct_answer = "yes" if is_prime_number(question) else "no"

    return {
        "question": question,
        "answer": correct_answer
    }