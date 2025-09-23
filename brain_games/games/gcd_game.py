from random import randint

from brain_games.utils import get_greatest_common_divisor


def game():
    first = randint(2, 20)
    second = randint(20, 50)
    question = f"{first} {second}"
    correct_answer = get_greatest_common_divisor(first, second)

    return {
        "question": question,
        "answer": f"{correct_answer}"
    }