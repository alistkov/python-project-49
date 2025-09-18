from random import choice, randint

from brain_games.utils import getGreatestCommonDivisor


def game():
    first = randint(2, 20)
    second = randint(20, 50)
    question = f"{first} {second}"
    correct_answer = getGreatestCommonDivisor(first, second)

    return {
        "question": question,
        "answer": f"{correct_answer}"
    }