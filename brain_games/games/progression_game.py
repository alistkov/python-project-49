from random import randint

from brain_games.utils import generateProgression


def game():
    start = randint(5, 20)
    step = randint(5, 9)
    progression_length = randint(5, 10)

    progression = generateProgression(start, step, progression_length)

    random_index = randint(0, progression_length - 1)

    correct_answer = progression[random_index]
    progression[random_index] = ".."
          
    return {
        "question": " ".join(map(str, progression)),
        "answer": f"{correct_answer}"
    }
