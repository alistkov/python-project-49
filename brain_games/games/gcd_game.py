from brain_games.utils import generate_random, get_greatest_common_divisor


def game():
    first = generate_random(2, 20)
    second = generate_random(20, 50)
    question = f"{first} {second}"
    correct_answer = get_greatest_common_divisor(first, second)

    return {
        "question": question,
        "answer": f"{correct_answer}"
    }