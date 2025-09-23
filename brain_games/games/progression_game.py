from brain_games.utils import generate_progression, generate_random


def game():
    start = generate_random(5, 20)
    step = generate_random(5, 9)
    progression_length = generate_random(5, 10)
    progression = generate_progression(start, step, progression_length)
    random_index = generate_random(0, progression_length - 1)

    correct_answer = progression[random_index]
    progression[random_index] = ".."
          
    return {
        "question": " ".join(map(str, progression)),
        "answer": f"{correct_answer}"
    }
